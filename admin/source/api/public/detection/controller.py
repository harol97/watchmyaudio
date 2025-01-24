from typing import Annotated

from fastapi import Query

from ...admin.client.depends import ClientDepends
from .depends import ReportFileGeneratorDepends, ServiceDepends
from .dtos import GetReportQuery


class Controller:
    async def get_report(
        self,
        service: ServiceDepends,
        client: ClientDepends,
        query: Annotated[GetReportQuery, Query()],
        reportfile_generator: ReportFileGeneratorDepends,
    ):
        detections = await service.get_report(
            client, query.start_date_utc, query.end_date_utc
        )

        return await reportfile_generator.generate_reportfile(detections)
