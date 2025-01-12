from pydantic import BaseModel


class LoginResponse(BaseModel):
    acces_token: str
    token_type: str
