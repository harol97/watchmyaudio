from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import SQLModel

from source.api import api_router
from source.dependencies.session import engine
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


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)
