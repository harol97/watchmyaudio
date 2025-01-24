from dataclasses import dataclass
from datetime import datetime
from typing import cast

from ...admin.client.dtos import Client
from .dtos import Report
from .repository import Repository
from .service import Service


@dataclass
class ServiceImplementation(Service):
    repository: Repository

    async def get_report(
        self, client: Client, start_date: datetime, end_date: datetime
    ) -> list[Report]:
        detections = await self.repository.get_detections_by_client(
            client.client_id, start_date, end_date
        )
        return [
            Report(
                client_name=detection.client.name,
                radio_station_name=detection.radio_station.name,
                filename=detection.advertisement.filename,
                advertisement_id=cast(int, detection.advertisement.advertisement_id),
                detection_date=detection.datetime_utc,
                timezone=detection.timezone,
            )
            for detection in detections
        ]
