from abc import ABC, abstractmethod
from typing import Sequence

from sqlmodel import SQLModel

from source.utils.base_repository import BaseRepository

from .model import ClientModel


class ClientModelUpdate(SQLModel):
    active: bool | None = None
    name: str | None = None
    password: str | None = None
    phone: str | None = None
    web: str | None = None
    language: str | None = None


class ClientRepository(ABC, BaseRepository):
    @abstractmethod
    async def get_active_all(self) -> Sequence[ClientModel]:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_email(self, email: str) -> ClientModel | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_active_by_email(self, email: str) -> ClientModel | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, client_id: int) -> ClientModel | None:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, new_client: ClientModel) -> ClientModel:
        raise NotImplementedError()

    @abstractmethod
    async def update(
        self, new_client: ClientModelUpdate, old_client: ClientModel
    ) -> ClientModel:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, client: ClientModel):
        raise NotImplementedError()
