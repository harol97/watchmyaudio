from csv import writer
from tempfile import NamedTemporaryFile
from typing import Annotated

from fastapi import Query

from ...admin.client.depends import ClientDepends
from .depends import ServiceDepends
from .dtos import GetReportQuery
from .responses import GetReportResponse


class Controller:
    async def get_report(
        self,
        service: ServiceDepends,
        client: ClientDepends,
        query: Annotated[GetReportQuery, Query()],
    ):
        title = ["Client", "Radio Station", "Filename", "Detection Date", "Timezone"]
        rows = [
            [
                report.client_name,
                report.radio_station_name,
                report.filename,
                report.detection_date,
                report.timezone,
            ]
            for report in await service.get_report(
                client, query.start_date_utc, query.end_date_utc
            )
        ]
        name = ""
        with NamedTemporaryFile(delete=False) as file:
            name = file.name
            with open(name, "w") as csv_file:
                csv_writer = writer(csv_file)
                csv_writer.writerow(title)
                csv_writer.writerows(rows)
        return GetReportResponse(name)
