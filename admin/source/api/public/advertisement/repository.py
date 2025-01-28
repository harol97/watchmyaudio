from abc import ABC, abstractmethod
from typing import Sequence

from sqlalchemy import ColumnExpressionArgument

from source.utils.custom_base_model import CustomBaseModel

from ....utils.base_repository import BaseRepository
from .model import AdvertisementModel


class UpdateDate(CustomBaseModel):
    active: bool | None = None


class Repository(ABC, BaseRepository):
    @abstractmethod
    async def create(self, new_advertisement: AdvertisementModel) -> AdvertisementModel:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_client(
        self, client_id: int, filters: list[ColumnExpressionArgument[bool]]
    ) -> Sequence[AdvertisementModel]:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, advertisement_id: int) -> AdvertisementModel | None:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, advertisement: AdvertisementModel):
        raise NotImplementedError()

    @abstractmethod
    async def update(
        self, advertisement: AdvertisementModel, data_to_update: UpdateDate
    ) -> AdvertisementModel:
        raise NotImplementedError()
