from sqlmodel import SQLModel

from source.utils.database_helpers import create_database_helper

from ..dependencies.session import engine
from .admin import create_user


async def execute_all():
    await create_database_helper(engine.url)
    SQLModel.metadata.create_all(engine)
    await create_user()
