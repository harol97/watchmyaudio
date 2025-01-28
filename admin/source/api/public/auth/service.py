from source.utils.token import AuthData, create_access_token

from ...admin.client.dtos import Client


class Service:
    def login(
        self,
        client: Client,
    ):
        access_token = create_access_token(
            data=AuthData(user_id=client.client_id, is_admin=False),
        )
        return dict(acces_token=access_token, token_type="Bearer")
