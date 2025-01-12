from abc import ABC, abstractmethod
from typing import Sequence

from sqlmodel import SQLModel

from source.utils.base_repository import BaseRepository

from .model import UserModel


class UserModelUpdate(SQLModel):
    name: str | None
    password: str | None


class UserRepository(ABC, BaseRepository):
    @abstractmethod
    async def get_all(self) -> Sequence[UserModel]:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_email(self, email: str) -> UserModel | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, user_id: int) -> UserModel | None:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, new_user: UserModel):
        raise NotImplementedError()

    @abstractmethod
    async def update(self, new_user: UserModelUpdate, old_user: UserModel) -> UserModel:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, user: UserModel):
        raise NotImplementedError()
