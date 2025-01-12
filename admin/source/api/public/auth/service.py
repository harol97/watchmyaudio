from datetime import timedelta

from source.utils.token import AuthData, create_access_token

from ...admin.client.dtos import Client
from .dtos import LoginResponse

ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Service:
    def login(
        self,
        client: Client,
    ):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data=AuthData(user_id=client.client_id, is_admin=False),
            expires_delta=access_token_expires,
        )
        return LoginResponse(acces_token=access_token, token_type="Bearer")
