from contextlib import asynccontextmanager
from datetime import datetime

from fastapi import FastAPI
from socketio import ASGIApp, AsyncServer
from sqlmodel import SQLModel

from source.api import api_router
from source.api.public.detection.model import Detection
from source.dependencies.session import engine, get_session
from source.utils.database_helpers import create_database_helper
from source.utils.scheduler import Scheduler


@asynccontextmanager
async def lifespan(_: FastAPI):
    await create_database_helper("sqlite:///database.db")
    SQLModel.metadata.create_all(engine)
    scheduler = Scheduler.get_instance().apscheduler
    scheduler.start()
    yield
    scheduler.shutdown(wait=False)


socket_server = AsyncServer(cors_allowed_origins="*", async_mode="asgi")
socket_app = ASGIApp(socket_server)

app = FastAPI(lifespan=lifespan)
app.include_router(api_router)
app.mount("/", socket_app)


@socket_server.event
async def join_room(sid, data):
    room_id = data["id"]
    await socket_server.enter_room(sid, str(room_id))
    await socket_server.emit("receive_data", data, room=str(room_id), skip_sid=sid)


@socket_server.event
async def leave_room(sid, data):
    room_id = data["id"]
    await socket_server.leave_room(sid, str(room_id))


@socket_server.event
async def send_message(sid, data: dict):
    await socket_server.emit("receive_data", data, room=str(data["id"]), skip_sid=sid)
    is_detection = data.get("is_detection", False)
    if is_detection:
        try:
            session = next(get_session())
            session.add(
                Detection(
                    datetime_utc=datetime.strptime(
                        data["datetime_detection"], "%Y-%m-%d %H:%M:%S"
                    ),
                    advertisement_id=data["advertisement_id"],
                    radio_station_id=data["radio_station_id"],
                    client_id=data["id"],
                    timezone=data["timezone"],
                )
            )
            session.commit()
        except:
            ...
