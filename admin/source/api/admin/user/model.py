from sqlalchemy import Integer
from sqlmodel import Column, Field, SQLModel


class UserModel(SQLModel, table=True):
    __tablename__ = "user"  # type: ignore

    user_id: int | None = Field(
        default=None,
        sa_column=Column(Integer, name="id", primary_key=True, autoincrement=True),
    )
    name: str
    email: str
    password: str
