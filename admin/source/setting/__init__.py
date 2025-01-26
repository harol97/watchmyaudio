from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    url: str = "sqlite:///database.db"
    docs_url: str | None = None


setting = Setting()  # type: ignore
