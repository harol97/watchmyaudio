from pydantic import EmailStr, SecretStr

from source.utils.custom_base_model import CustomBaseModel


class UserIn(CustomBaseModel):
    name: str
    email: EmailStr
    password: str


class UpdateBody(CustomBaseModel):
    name: str | None = None
    password: str | None = None


class User(CustomBaseModel):
    user_id: int
    name: str
    email: EmailStr
    password: SecretStr
