from datetime import timedelta

from source.utils.token import AuthData, create_access_token

from ..user.dtos import User
from .dtos import LoginResponse

ACCESS_TOKEN_EXPIRE_MINUTES = 43800


class Service:
    def login(self, user: User):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data=AuthData(user_id=user.user_id, is_admin=True),
            expires_delta=access_token_expires,
        )
        return LoginResponse(acces_token=access_token, token_type="Bearer")
