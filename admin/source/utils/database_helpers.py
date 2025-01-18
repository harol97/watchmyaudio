from pydantic.networks import HttpUrl
from sqlalchemy import URL
from sqlalchemy.types import TypeDecorator
from sqlalchemy_utils.functions.database import create_database, database_exists
from sqlmodel import String


async def create_database_helper(url: str | URL):
    if not database_exists(url):
        create_database(url)


class HttpUrlType(TypeDecorator):
    impl = String(2083)
    cache_ok = True

    def process_bind_param(self, value, dialect) -> str:
        return str(value)

    def process_result_value(self, value, dialect) -> HttpUrl:
        return HttpUrl(url=str(value))

    def process_literal_param(self, value, dialect) -> str:
        return str(value)
