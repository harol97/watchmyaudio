from sqlmodel import SQLModel, text

from source.utils.database_helpers import create_database_helper

from ..dependencies.session import engine
from .admin import create_user


async def execute_all():
    await create_database_helper(engine.url)
    SQLModel.metadata.create_all(engine)
    with engine.connect() as connection:
        connection.execute(text("PRAGMA foreign_keys=ON"))
    await create_user()
