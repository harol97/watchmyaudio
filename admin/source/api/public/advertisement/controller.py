from datetime import datetime
from typing import Annotated
from uuid import uuid4

from fastapi import File, Form, HTTPException, Query, UploadFile, status
from pydantic_extra_types.timezone_name import TimeZoneName

from source.utils.timezone_utlis import to_utc

from ...admin.client.depends import ClientDepends
from ...admin.radio_station.depends import ServiceDepends as RadioStationServiceDepends
from .depends import FileSaverDepends, ServiceDepends
from .dtos import AdvertisementIn
from .requests import FilterQuery, UpdateQuery


class Controller:
    async def get_by_client(
        self,
        service: ServiceDepends,
        query: Annotated[FilterQuery, Query()],
        client: ClientDepends,
    ):
        return await service.get_by_client(client, query)

    async def create(
        self,
        service: ServiceDepends,
        radio_station_service: RadioStationServiceDepends,
        client: ClientDepends,
        file_saver: FileSaverDepends,
        radio_station_id: Annotated[list[int], Form()],
        timezone: Annotated[TimeZoneName, Form()],
        name: Annotated[str, Form(default_factory=lambda: str(uuid4()))],
        file: UploadFile = File(),
        start_date: Annotated[datetime | None, Form()] = None,
        end_date: Annotated[datetime | None, Form()] = None,
    ):
        if start_date:
            start_date = to_utc(start_date, timezone)

        if end_date:
            end_date = to_utc(end_date, timezone)

        body = AdvertisementIn(
            name=name,
            radio_stations_ids=radio_station_id,
            start_date=start_date,
            end_date=end_date,
            filename_in_system=f"{uuid4()}.mp3",
        )
        radio_stations = await radio_station_service.get_by_ids(body.radio_stations_ids)
        if len(radio_stations) != len(body.radio_stations_ids):
            raise HTTPException(status.HTTP_409_CONFLICT)
        return await service.create(
            file, body, client, radio_stations, file_saver, timezone_client=timezone
        )

    async def delete(
        self,
        service: ServiceDepends,
        advertisement_id: int,
        file_saver: FileSaverDepends,
    ):
        advertisement = await service.get_by_id(advertisement_id)
        await service.delete(advertisement)
        await file_saver.delete(advertisement.filename_in_system)
        return dict()

    async def update(
        self,
        service: ServiceDepends,
        advertisement_id: int,
        query: Annotated[UpdateQuery, Query()],
    ):
        advertisement = await service.get_by_id(advertisement_id)
        return await service.patch(advertisement, query.model_dump(exclude_none=True))
