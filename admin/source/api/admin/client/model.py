from typing import Literal

from pydantic import HttpUrl
from sqlmodel import Column, Field, Integer, SQLModel

from source.utils.database_helpers import HttpUrlType

ClientKind = Literal["UNDEFINED", "SCHEDULE"]


class ClientModel(SQLModel, table=True):
    __tablename__ = "client"  # type: ignore

    client_id: int | None = Field(
        default=None,
        alias="id",
        sa_column=Column(Integer, name="id", primary_key=True, autoincrement=True),
    )
    name: str
    email: str = Field(unique=True)
    kind: str
    password: str
    phone: str | None = None
    web: HttpUrl | None = Field(default=None, sa_type=HttpUrlType)
    language: str
    active: bool = Field(default=True)
