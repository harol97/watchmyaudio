from datetime import datetime, timezone
from difflib import SequenceMatcher
from tempfile import NamedTemporaryFile
from typing import Literal

import ffmpeg
import librosa
import pytz
import torch
from socketio import Client
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

from source.utils.scheduler import Scheduler

from ...admin.radio_station.dtos import RadioStation
from .dtos import Advertisement

# Cargar modelo Wav2Vec2 en español


def transcribe(audio_path, processor, model):
    speech, rate = librosa.load(audio_path, sr=16000)
    input_values = processor(
        speech, sampling_rate=int(rate), return_tensors="pt"
    ).input_values  # type: ignore
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])  # type: ignore
    return transcription


# Función para capturar un fragmento del stream
def stream_to_audio(input_url, duration=10):
    process = (
        ffmpeg.input(input_url)
        .output("-", format="wav", acodec="pcm_s16le", ac=1, ar="16000", t=duration)
        .run(capture_stdout=True, capture_stderr=True)
    )
    return process[0]


# Función para calcular la similitud entre dos textos
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


def process_advertisement(
    job_id: str,
    user_id: int,
    advertisement: Advertisement,
    radio_station: RadioStation,
    end_date: datetime | None,
    timezone_client: str,
    language: Literal["NEPALI", "ENGLISH"],
):
    sio = Client()
    sio.connect("http://localhost:8000")

    sio.emit(
        "join_room",
        {
            "id": user_id,
            "message": "Analyzing..",
            "radio_station": radio_station.name,
            "advertisement": advertisement.filename,
        },
    )
    model_name = "facebook/wav2vec2-large-960h"
    if language == "NEPALI":
        model_name = "gagan3012/wav2vec2-xlsr-nepali"

    processor = Wav2Vec2Processor.from_pretrained(model_name)
    model = Wav2Vec2ForCTC.from_pretrained(model_name)
    # Archivo de anuncio comercial
    ad_transcription = transcribe(advertisement.filename_in_system, processor, model)
    stream_url = str(radio_station.url)
    threshold = 0.5  # Umbral de similitud
    fragment_duration = 10  # Duración de cada fragmento en segundos

    scheduler = Scheduler.get_instance()
    # Definir la zona horaria de Nepal

    while True:
        # Capturar un fragmento del stream en memoria
        if end_date:
            current_datetime = datetime.now(timezone.utc)
            if current_datetime >= end_date:
                return

        if scheduler.should_process_job_finish(job_id):
            return

        audio_data = stream_to_audio(stream_url, duration=fragment_duration)

        # Guardar el fragmento temporalmente en memoria
        with NamedTemporaryFile() as temp_file:
            name = temp_file.name
            with open(name, "wb") as f:
                f.write(audio_data)
            # Transcribir el fragmento del stream
            fragment_transcription = transcribe(name, processor, model)

            # Comparar las transcripciones
            similarity_score = similarity(ad_transcription, fragment_transcription)

            # Evaluar si el anuncio fue detectado
            if similarity_score > threshold:
                detection_time_obj = datetime.now(timezone.utc)
                detection_time = detection_time_obj.strftime("%Y-%m-%d %H:%M:%S")
                client_timezone = pytz.timezone(timezone_client)
                detection_time_in_client_timezone = detection_time_obj.astimezone(
                    client_timezone
                )
                sio.emit(
                    "send_message",
                    {
                        "message": f"Detection at {detection_time_in_client_timezone} {timezone_client}",
                        "datetime_detection": detection_time,
                        "id": user_id,
                        "radio_station": radio_station.name,
                        "advertisement_id": advertisement.advertisement_id,
                        "radio_station_id": radio_station.radio_station_id,
                        "advertisement": advertisement.filename,
                        "is_detection": True,
                        "timezone": timezone_client,
                    },
                )
                sio.emit(
                    "send_message",
                    {
                        "message": "Analyzing...",
                        "id": user_id,
                        "radio_station": radio_station.name,
                        "advertisement": advertisement.filename,
                    },
                )
