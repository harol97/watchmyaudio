from typing import Annotated, Literal

from pydantic import EmailStr, Field, SecretStr
from pydantic.networks import HttpUrl

from source.utils.custom_base_model import CustomBaseModel

from .model import ClientKind


class ClientIn(CustomBaseModel):
    name: str
    email: EmailStr
    password: str
    kind: ClientKind
    web: HttpUrl | None = None
    language: str
    phone: str | None = None


class UpdateBody(CustomBaseModel):
    name: str | None = None
    password: str | None = None
    kind: ClientKind | None = None
    web: HttpUrl | None = None
    language: str | None = None
    phone: str | None = None


class Client(CustomBaseModel):
    client_id: Annotated[int, Field(alias="id")]
    name: str
    email: EmailStr
    password: SecretStr
    kind: ClientKind
    web: HttpUrl | None
    language: Literal["NEPALI", "ENGLISH"]
    phone: str | None
