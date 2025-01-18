from typing import Annotated

from pydantic import Field

from source.utils.custom_base_model import CustomBaseModel


class LoginResponse(CustomBaseModel):
    acces_token: Annotated[str, Field(alias="accesToken")]
    token_type: str = Field(alias="tokenType")
