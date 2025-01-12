from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from ..user.depends import ServiceDepends as UserServiceDepends
from .service import Service


class Controller:
    def __init__(self, service: Service) -> None:
        self.service = service

    async def login(
        self,
        form: Annotated[OAuth2PasswordRequestForm, Depends()],
        user_service: UserServiceDepends,
    ):
        user = await user_service.valid_account(form.username, form.password)
        return self.service.login(user)
