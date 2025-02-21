from dataclasses import dataclass
from datetime import datetime
from itertools import groupby
from random import choice
from typing import cast

from ...admin.client.dtos import Client
from .custom_colors import colors
from .dtos import Report
from .repository import Repository
from .responses import GetDataResponse
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

    async def get_data(
        self, client: Client, start_date: datetime, end_date: datetime
    ) -> list[GetDataResponse]:
        detections = await self.repository.get_detections_by_client(
            client.client_id, start_date, end_date
        )
        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        result: list[GetDataResponse] = []
        for _, detections_grouped in groupby(
            detections, lambda detection: detection.advertisement_id
        ):
            detections_grouped_as_tuple = tuple(detections_grouped)
            data_per_month = [
                len(
                    tuple(
                        filter(
                            lambda detection: detection.datetime_utc.month == month,
                            detections_grouped_as_tuple,
                        )
                    )
                )
                for month in months
            ]
            response = GetDataResponse(
                song=detections_grouped_as_tuple[0].advertisement.filename,
                data_per_month=data_per_month,
                color=choice(colors).as_string(255),
            )
            result.append(response)
        return result
