from source.utils.custom_base_model import CustomBaseModel


class LoginResponse(CustomBaseModel):
    acces_token: str
    token_type: str
