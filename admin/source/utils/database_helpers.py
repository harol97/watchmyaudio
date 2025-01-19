from pydantic.networks import HttpUrl
from sqlalchemy import URL, String
from sqlalchemy.types import TypeDecorator
from sqlalchemy_utils.functions.database import create_database, database_exists


async def create_database_helper(url: str | URL):
    if not database_exists(url):
        create_database(url)


class HttpUrlType(TypeDecorator):
    impl = String(2083)
    cache_ok = True

    def process_bind_param(self, value: str | None, dialect) -> str | None:
        if not value:
            return None
        return str(value)

    def process_result_value(self, value: str | None, dialect) -> HttpUrl | None:
        if not value:
            return None
        print("no????", value)
        return HttpUrl(url=value)

    def process_literal_param(self, value: str | None, dialect) -> str:
        return str(value)
