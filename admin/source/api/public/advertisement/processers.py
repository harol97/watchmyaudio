import os
from datetime import datetime, tzinfo
from difflib import SequenceMatcher
from uuid import uuid4

import ffmpeg
import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

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
    advertisement: Advertisement, radio_station: RadioStation, end_date: datetime | None
):
    model_name = "facebook/wav2vec2-large-960h"
    processor = Wav2Vec2Processor.from_pretrained(model_name)
    model = Wav2Vec2ForCTC.from_pretrained(model_name)
    # Archivo de anuncio comercial
    ad_transcription = transcribe(advertisement.filename, processor, model)

    # URL del stream
    # stream_url = "https://cdnhd.iblups.com/hls/0773874174fd4eba8bb9eff741d190dc.m3u8"
    stream_url = "https://live.itech.host:3225/stream"
    stream_url = str(radio_station.url)

    # Parámetros de detección
    threshold = 0.5  # Umbral de similitud
    fragment_duration = 10  # Duración de cada fragmento en segundos

    # Definir la zona horaria de Nepal
    end_date_local_time = None
    if end_date:
        end_date_local_time = tzinfo().fromutc(end_date)

    while True:
        # Capturar un fragmento del stream en memoria
        if end_date_local_time:
            current_datetime = datetime.now()
            if current_datetime >= end_date_local_time:
                return

        audio_data = stream_to_audio(stream_url, duration=fragment_duration)

        # Guardar el fragmento temporalmente en memoria
        name = f"{uuid4()}.wav"
        with open(name, "wb") as f:
            f.write(audio_data)

        # Transcribir el fragmento del stream
        fragment_transcription = transcribe(name, processor, model)

        # Comparar las transcripciones
        similarity_score = similarity(ad_transcription, fragment_transcription)

        # Evaluar si el anuncio fue detectado
        if similarity_score > threshold:
            detection_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Ad detected in the stream! Time: {detection_time} (Nepal Timezone)")

        # Limpiar el archivo temporal
        os.remove(name)
