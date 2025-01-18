from csv import writer
from tempfile import NamedTemporaryFile

from ...admin.client.depends import ClientDepends
from .depends import ServiceDepends
from .responses import GetReportResponse


class Controller:
    async def get_report(self, service: ServiceDepends, client: ClientDepends):
        title = ["Client", "Radio Station", "Filename", "Detection Date"]
        rows = [
            [
                report.client_name,
                report.radio_station_name,
                report.filename,
                report.detection_date,
            ]
            for report in await service.get_report(client)
        ]
        name = ""
        with NamedTemporaryFile(delete=False) as file:
            name = file.name
            with open(name, "w") as csv_file:
                csv_writer = writer(csv_file)
                csv_writer.writerow(title)
                csv_writer.writerows(rows)
        return GetReportResponse(name)
