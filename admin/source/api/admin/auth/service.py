from source.utils.token import AuthData, create_access_token

from ..user.dtos import User
from .dtos import LoginResponse


class Service:
    def login(self, user: User):
        access_token = create_access_token(
            data=AuthData(user_id=user.user_id, is_admin=True),
        )
        return LoginResponse(acces_token=access_token, token_type="Bearer")
