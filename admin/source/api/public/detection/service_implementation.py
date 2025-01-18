from dataclasses import dataclass

from ...admin.client.dtos import Client
from .dtos import Report
from .repository import Repository
from .service import Service


@dataclass
class ServiceImplementation(Service):
    repository: Repository

    async def get_report(self, client: Client) -> list[Report]:
        detections = await self.repository.get_detections_by_client(client.client_id)
        return [
            Report(
                client_name=detection.client.name,
                radio_station_name=detection.radio_station.name,
                filename=detection.advertisement.filename,
                detection_date=detection.datetime_utc,
            )
            for detection in detections
        ]
