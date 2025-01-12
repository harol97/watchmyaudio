from abc import ABC, abstractmethod
from typing import Sequence

from pydantic import HttpUrl

from ..user.dtos import User
from .dtos import RadioStation


class Service(ABC):
    @abstractmethod
    @abstractmethod
    async def create(self, url: HttpUrl, user: User) -> RadioStation:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, radio_station_id: int) -> RadioStation:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, radio_station: RadioStation) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_ids(self, ids: list[int]) -> Sequence[RadioStation]:
        raise NotImplementedError()
