from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Sequence, cast

from fastapi import HTTPException, UploadFile, status
from pydantic import TypeAdapter
from sqlmodel import col

from source.utils.scheduler import Scheduler

from ...admin.client.dtos import Client
from ...admin.radio_station.dtos import RadioStation
from ..analyzer.model import AnalyzerModel
from ..analyzer.repository import Repository as AnalyzerRepository
from .dtos import Advertisement, AdvertisementIn
from .model import AdvertisementModel
from .processers import process_advertisement
from .repository import Repository, UpdateDate
from .requests import FilterQuery
from .save_advertisement import AdvertisementSaver
from .service import Service

AdvertisementListAdapter = TypeAdapter(Sequence[Advertisement])


@dataclass
class ServiceImplementation(Service):
    repository: Repository
    analyzer_repository: AnalyzerRepository

    async def create(
        self,
        file: UploadFile,
        body: AdvertisementIn,
        client: Client,
        radio_stations,
        saver_file: AdvertisementSaver,
        timezone_client: str,
    ) -> Advertisement:
        await saver_file.save(file.file, body.filename_in_system)

        if client.kind == "UNDEFINED":
            body.end_date = None

        new_advertisement = await self.repository.create(
            AdvertisementModel(
                filename=f"{file.filename}",
                client_id=client.client_id,
                name=body.name,
                filename_in_system=body.filename_in_system,
            )
        )
        advertisement_dto = Advertisement.model_validate(new_advertisement)

        if not new_advertisement.advertisement_id:
            raise HTTPException(status.HTTP_409_CONFLICT)

        if client.kind == "UNDEFINED":
            start_date = datetime.now(timezone.utc) + timedelta(seconds=20)
        else:
            if not body.start_date or not body.end_date:
                raise HTTPException(status.HTTP_400_BAD_REQUEST)
            start_date = body.start_date

        self.analyzer_repository.create_many(
            [
                await self.build_analyzer_obj(
                    advertisement_dto,
                    radio_station,
                    timezone_client,
                    client.language,
                    advertisement_id=new_advertisement.advertisement_id,
                    client_id=client.client_id,
                    radio_station_id=radio_station.radio_station_id,
                    start_date=start_date,
                    end_date=body.end_date,
                )
                for radio_station in radio_stations
            ]
        )
        self.repository.commit()
        return advertisement_dto

    async def build_analyzer_obj(
        self,
        advertisement: Advertisement,
        radio_station: RadioStation,
        timezone_client: str,
        language: str,
        **args,
    ) -> AnalyzerModel:
        job = Scheduler.get_instance().append_job(
            process_advertisement,
            args["start_date"],
            *[
                args["client_id"],
                advertisement,
                radio_station,
                args["end_date"],
                timezone_client,
                language,
            ],
        )
        return AnalyzerModel(**{**args, "job_id": job.id})

    async def get_by_client(
        self, client: Client, query: FilterQuery
    ) -> Sequence[Advertisement]:
        advertisements = await self.repository.get_by_client(
            client.client_id, filters=[col(AdvertisementModel.active) == query.active]
        )
        return AdvertisementListAdapter.validate_python(advertisements)

    async def get_by_id(self, advertisement_id: int) -> Advertisement:
        advertisement = await self.repository.get_by_id(advertisement_id)
        if not advertisement:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return Advertisement.model_validate(advertisement)

    async def delete(self, advertisement: Advertisement):
        await self.repository.delete(
            cast(
                AdvertisementModel,
                await self.repository.get_by_id(advertisement.advertisement_id),
            )
        )
        self.repository.commit()
        analyzers = await self.analyzer_repository.get_by_advertisement(
            advertisement.advertisement_id
        )
        self.repository.commit()
        scheduler = Scheduler.get_instance()
        for analyzer in analyzers:
            scheduler.delete_job(analyzer.job_id)

    async def patch(
        self, advertisement: Advertisement, data_to_update: dict
    ) -> Advertisement:
        advertisement_model = cast(
            AdvertisementModel,
            await self.repository.get_by_id(advertisement.advertisement_id),
        )
        advertisement_updated = await self.repository.update(
            advertisement_model, UpdateDate.model_validate(data_to_update)
        )

        self.repository.commit()
        if data_to_update.get("active") is False:
            analyzers = await self.analyzer_repository.get_by_advertisement(
                advertisement.advertisement_id
            )
            scheduler = Scheduler.get_instance()
            for analyzer in analyzers:
                scheduler.delete_job(analyzer.job_id)
        return Advertisement.model_validate(advertisement_updated)
