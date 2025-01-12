from abc import ABC, abstractmethod
from typing import Sequence

from ....utils.base_repository import BaseRepository
from .model import AdvertisementModel


class Repository(ABC, BaseRepository):
    @abstractmethod
    async def create(self, new_advertisement: AdvertisementModel) -> AdvertisementModel:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_client(self, client_id: int) -> Sequence[AdvertisementModel]:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, advertisement_id: int) -> AdvertisementModel | None:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, advertisement: AdvertisementModel):
        raise NotImplementedError()
