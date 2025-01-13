from sqlalchemy import URL
from sqlalchemy_utils.functions.database import create_database, database_exists


async def create_database_helper(url: str | URL):
    if not database_exists(url):
        create_database(url)
