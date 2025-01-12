from typing import Annotated

from pydantic import EmailStr, Field, SecretStr

from source.utils.custom_base_model import CustomBaseModel

from .model import ClientKind


class ClientIn(CustomBaseModel):
    name: str
    email: EmailStr
    password: str
    kind: ClientKind


class UpdateBody(CustomBaseModel):
    name: str | None = None
    password: str | None = None
    kind: ClientKind | None = None


class Client(CustomBaseModel):
    client_id: Annotated[int, Field(alias="id")]
    name: str
    email: EmailStr
    password: SecretStr
    kind: ClientKind
