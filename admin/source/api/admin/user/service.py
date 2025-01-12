from abc import ABC, abstractmethod
from typing import Sequence

from .dtos import UpdateBody, User, UserIn


class Service(ABC):
    @abstractmethod
    async def create(self, new_user: UserIn) -> User:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, data: UpdateBody, user_id: int) -> User:
        raise NotImplementedError()

    @abstractmethod
    async def get_all(self) -> Sequence[User]:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, user_id: int) -> User:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_email(self, email: str) -> User:
        raise NotImplementedError()

    @abstractmethod
    async def valid_account(self, email: str, password: str) -> User:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, user_id: int):
        raise NotImplementedError()
