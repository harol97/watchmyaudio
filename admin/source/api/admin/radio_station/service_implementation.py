from typing import Sequence, cast

from fastapi import HTTPException, status
from pydantic import HttpUrl, TypeAdapter

from source.utils.scheduler import Scheduler

from ...public.analyzer.repository import Repository as AnalyzerRepository
from ..user.dtos import User
from .dtos import RadioStation
from .model import RadioStationModel
from .repository import Repository
from .service import Service

validator_sequence = TypeAdapter(Sequence[RadioStation])


class ServiceImplementation(Service):
    def __init__(
        self, repository: Repository, analyzer_repository: AnalyzerRepository
    ) -> None:
        self.repository = repository
        self.analyzer_repository = analyzer_repository

    async def create(self, url: HttpUrl, name: str, user: User) -> RadioStation:
        new_radio_station = await self.repository.create(
            RadioStationModel(url=str(url), user_id=user.user_id, name=name)
        )
        self.repository.commit()
        return RadioStation.model_validate(new_radio_station)

    async def get_by_id(self, radio_station_id: int) -> RadioStation:
        radio_station = await self.repository.get_by_id(radio_station_id)
        if not radio_station:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return RadioStation.model_validate(radio_station)

    async def delete(self, radio_station: RadioStation):
        await self.repository.delete(
            cast(
                RadioStationModel,
                await self.repository.get_by_id(radio_station.radio_station_id),
            )
        )
        analyzers = await self.analyzer_repository.get_by_radio_station(
            radio_station_id=radio_station.radio_station_id
        )
        scheduler = Scheduler.get_instance()
        for analyzer in analyzers:
            scheduler.delete_job(analyzer.job_id)
        self.repository.commit()

    async def get_by_ids(self, ids: list[int]) -> Sequence[RadioStation]:
        return validator_sequence.validate_python(await self.repository.get_by_ids(ids))

    async def get_all(self) -> Sequence[RadioStation]:
        return validator_sequence.validate_python(await self.repository.get_all())
