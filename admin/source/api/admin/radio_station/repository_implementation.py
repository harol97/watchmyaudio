from dataclasses import dataclass
from typing import Sequence

from sqlmodel import col, select

from .model import RadioStationModel
from .repository import Repository


@dataclass
class RepositoryImplementation(Repository):
    async def create(self, new_radio_station: RadioStationModel) -> RadioStationModel:
        self.session.add(new_radio_station)
        self.session.flush()
        return new_radio_station

    async def get_by_id(self, radio_station_id: int) -> RadioStationModel | None:
        return self.session.exec(
            select(RadioStationModel).where(
                RadioStationModel.radio_station_id == radio_station_id
            )
        ).first()

    async def delete(self, radio_station: RadioStationModel):
        self.session.delete(radio_station)

    async def get_by_ids(self, ids: list[int]):
        return self.session.exec(
            select(RadioStationModel).where(
                col(RadioStationModel.radio_station_id).in_(ids)
            )
        ).all()

    async def get_all(self) -> Sequence[RadioStationModel]:
        return self.session.exec(select(RadioStationModel)).all()
