from dataclasses import dataclass
from typing import Sequence

from sqlalchemy import ColumnExpressionArgument
from sqlmodel import and_, col, select

from .model import AdvertisementModel
from .repository import Repository, UpdateDate


@dataclass
class RepositoryImplementation(Repository):
    async def create(self, new_advertisement: AdvertisementModel) -> AdvertisementModel:
        self.session.add(new_advertisement)
        self.session.flush()
        return new_advertisement

    async def get_by_client(
        self, client_id: int, filters: list[ColumnExpressionArgument[bool]]
    ) -> Sequence[AdvertisementModel]:
        return self.session.exec(
            select(AdvertisementModel).where(
                and_(col(AdvertisementModel.client_id) == client_id, *filters)
            )
        ).all()

    async def get_by_id(self, advertisement_id: int) -> AdvertisementModel | None:
        return self.session.exec(
            select(AdvertisementModel).where(
                AdvertisementModel.advertisement_id == advertisement_id
            )
        ).first()

    async def delete(self, advertisement: AdvertisementModel):
        self.session.delete(advertisement)

    async def update(
        self, advertisement: AdvertisementModel, data_to_update: UpdateDate
    ) -> AdvertisementModel:
        advertisement.sqlmodel_update(data_to_update.model_dump(exclude_none=True))
        self.session.add(advertisement)
        self.session.flush()
        return advertisement
