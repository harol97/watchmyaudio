from abc import ABC, abstractmethod
from typing import Sequence

from fastapi import UploadFile

from ...admin.client.dtos import Client
from ...admin.radio_station.dtos import RadioStation
from .dtos import Advertisement, AdvertisementIn
from .save_advertisement import AdvertisementSaver


class Service(ABC):
    @abstractmethod
    async def get_by_client(self, client: Client) -> Sequence[Advertisement]:
        raise NotImplementedError()

    @abstractmethod
    async def create(
        self,
        file: UploadFile,
        body: AdvertisementIn,
        client: Client,
        radio_stations: Sequence[RadioStation],
        saver_file: AdvertisementSaver,
    ) -> Advertisement:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, advertisement_id: int) -> Advertisement:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, advertisement: Advertisement) -> None:
        raise NotImplementedError()
