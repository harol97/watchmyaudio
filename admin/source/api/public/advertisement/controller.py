from datetime import datetime
from typing import Annotated

from fastapi import Form, HTTPException, UploadFile, status

from ...admin.client.depends import ClientDepends
from ...admin.radio_station.depends import ServiceDepends as RadioStationServiceDepends
from .depends import FileSaverDepends, ServiceDepends
from .dtos import AdvertisementIn


class Controller:
    async def get_by_client(self, service: ServiceDepends, client: ClientDepends):
        return service.get_by_client(client)

    async def create(
        self,
        service: ServiceDepends,
        radio_station_service: RadioStationServiceDepends,
        file: UploadFile,
        name: Annotated[str, Form()],
        radio_station_ids: Annotated[list[int], Form()],
        start_date: Annotated[datetime | None, Form()],
        end_date: Annotated[datetime | None, Form()],
        client: ClientDepends,
        file_saver: FileSaverDepends,
    ):
        body = AdvertisementIn(
            name=name,
            radio_stations_ids=radio_station_ids,
            start_date=start_date,
            end_date=end_date,
        )
        radio_stations = await radio_station_service.get_by_ids(body.radio_stations_ids)

        if len(radio_stations) != len(body.radio_stations_ids):
            raise HTTPException(status.HTTP_409_CONFLICT)
        return await service.create(file, body, client, radio_stations, file_saver)

    async def delete(self, service: ServiceDepends, advertisement_id: int):
        advertisement = await service.get_by_id(advertisement_id)
        return await service.delete(advertisement)
