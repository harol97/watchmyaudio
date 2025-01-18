from datetime import datetime
from datetime import timezone as tz
from typing import Annotated
from uuid import uuid4

import pytz
from fastapi import File, Form, HTTPException, UploadFile, status
from pydantic_extra_types.timezone_name import TimeZoneName

from ...admin.client.depends import ClientDepends
from ...admin.radio_station.depends import ServiceDepends as RadioStationServiceDepends
from .depends import FileSaverDepends, ServiceDepends
from .dtos import AdvertisementIn


class Controller:
    async def get_by_client(self, service: ServiceDepends, client: ClientDepends):
        return await service.get_by_client(client)

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
            local = pytz.timezone(timezone)
            local_dt = local.localize(start_date, is_dst=None)
            start_date = local_dt.astimezone(pytz.utc)

        if end_date:
            local = pytz.timezone(timezone)
            local_dt = local.localize(end_date, is_dst=None)
            end_date = local_dt.astimezone(pytz.utc)

        body = AdvertisementIn(
            name=name,
            radio_stations_ids=radio_station_id,
            start_date=start_date,
            end_date=end_date,
        )
        radio_stations = await radio_station_service.get_by_ids(body.radio_stations_ids)
        if len(radio_stations) != len(body.radio_stations_ids):
            raise HTTPException(status.HTTP_409_CONFLICT)
        return await service.create(file, body, client, radio_stations, file_saver)

    async def delete(self, service: ServiceDepends, advertisement_id: int):
        advertisement = await service.get_by_id(advertisement_id)
        await service.delete(advertisement)
        return dict()
