from dataclasses import dataclass
from typing import Sequence

from sqlmodel import select

from .model import AdvertisementModel
from .repository import Repository


@dataclass
class RepositoryImplementation(Repository):
    async def create(self, new_advertisement: AdvertisementModel) -> AdvertisementModel:
        self.session.add(new_advertisement)
        self.session.flush()
        return new_advertisement

    async def get_by_client(self, client_id: int) -> Sequence[AdvertisementModel]:
        return self.session.exec(
            select(AdvertisementModel).where(AdvertisementModel.client_id == client_id)
        ).all()

    async def get_by_id(self, advertisement_id: int) -> AdvertisementModel | None:
        return self.session.exec(
            select(AdvertisementModel).where(
                AdvertisementModel.advertisement_id == advertisement_id
            )
        ).first()

    async def delete(self, advertisement: AdvertisementModel):
        self.session.delete(advertisement)
