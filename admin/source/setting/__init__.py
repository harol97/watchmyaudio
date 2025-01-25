from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    url: str
    docs_url: str | None = None


setting = Setting()  # type: ignore
