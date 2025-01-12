from abc import ABC, abstractmethod
from typing import Sequence

from ....utils.base_repository import BaseRepository
from .model import RadioStationModel


class Repository(ABC, BaseRepository):
    @abstractmethod
    async def create(self, new_radio_station: RadioStationModel) -> RadioStationModel:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, radio_station_id: int) -> RadioStationModel | None:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, radio_station: RadioStationModel):
        raise NotImplementedError()

    @abstractmethod
    async def get_by_ids(self, ids: list[int]) -> Sequence[RadioStationModel]:
        raise NotImplementedError()
