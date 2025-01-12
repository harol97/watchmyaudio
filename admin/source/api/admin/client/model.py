from typing import Literal

from sqlmodel import Column, Field, Integer, SQLModel

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
