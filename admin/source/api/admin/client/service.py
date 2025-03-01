from abc import ABC, abstractmethod
from typing import Sequence

from ..radio_station.dtos import RadioStation
from .dtos import Client, ClientIn, UpdateBody


class Service(ABC):
    @abstractmethod
    async def create(self, new_client: ClientIn) -> Client:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, data: UpdateBody, client_id: int) -> Client:
        raise NotImplementedError()

    @abstractmethod
    async def get_active_all(self) -> Sequence[Client]:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, client_id: int) -> Client:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_email(self, email: str) -> Client:
        raise NotImplementedError()

    @abstractmethod
    async def valid_account(self, email: str, password: str) -> Client:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, client_id: int):
        raise NotImplementedError()

    @abstractmethod
    async def get_radio_stations(self, client_id: int) -> list[RadioStation]:
        raise NotImplementedError()
