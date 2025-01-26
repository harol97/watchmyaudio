from dataclasses import dataclass
from datetime import datetime
from itertools import groupby
from random import choice
from tempfile import NamedTemporaryFile
from reportlab.graphics.charts.linecharts import HorizontalLineChart

from fastapi.responses import FileResponse
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing
from reportlab.lib.colors import black
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.platypus.tables import Table

from source.utils.timezone_utlis import to_timezone

from .custom_colors import CustomColor, colors
from .dtos import Report
from .reportfile_generator import ReportFileGenerator


@dataclass
class Item:
    times: int
    filename: str
    color: CustomColor


class PdfGenerator(ReportFileGenerator):
    def __init__(self) -> None:
        self.temp_file = NamedTemporaryFile(suffix=".pdf", delete=False)

    def get_max(self, number, init=10):
        return init / 10 if number <= 0 else self.get_max(number // init, init * 10)

    async def generate_reportfile(self, detections: list[Report]) -> FileResponse:
        canva = canvas.Canvas(self.temp_file, pagesize=A4)
        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        data_per_month = []
        if detections:
            items: list[Item] = []
            y_max = 0
            for group in groupby(
                detections, key=lambda detection: detection.advertisement_id
            ):
                items_ids = tuple(group[1])

                number_of_detections = len(items_ids)
                if y_max < number_of_detections:
                    y_max = number_of_detections
                items.append(
                    Item(
                        times=number_of_detections,
                        filename=items_ids[0].filename,
                        color=choice(colors),
                    )
                )
                data_per_month.append(
                    list(
                        map(
                            lambda month: len(
                                tuple(
                                    filter(
                                        lambda detection: detection.detection_date.month
                                        == month,
                                        items_ids,
                                    )
                                )
                            ),
                            months,
                        )
                    )
                )

            xi, yi = 0, A4[1] - 50
            title = "Graphic Report Distribution (Bar Chart)"
            width_title = stringWidth(title, "Helvetica-Bold", 16)
            canva.drawString((A4[0] - width_title) / 2, yi, title)
            print(data_per_month)
            # vertical bar
            bc = HorizontalLineChart()
            bc.height = 200
            bc.strokeColor = black
            bc.width = int(A4[0]) - 50
            bc.data = data_per_month
            limit = self.get_max(y_max)
            bc.valueAxis.valueMin = 0
            bc.valueAxis.valueMax = limit
            bc.valueAxis.valueStep = limit / 10
            bc.groupSpacing = 10
            bc.categoryAxis.labels.boxAnchor = "ne"
            bc.categoryAxis.labels.angle = 70
            bc.categoryAxis.categoryNames = "Jan Feb Mar Apr May Jun Jul Aug".split(" ")
            for index, item in enumerate(items):
                bc.lines[index].strokeColor = item.color.rgb
            drawing = Drawing()
            drawing.add(bc)
            drawing.drawOn(canva, xi, yi - 20 - bc.height)
            # vertical bar

            # details
            yi_details = yi - bc.height - 100
            canva.drawString(
                xi + 10,
                yi_details,
                "Details:",
            )
            yi_details -= 20
            for item in items:
                canva.setFillColor(item.color.rgb)
                canva.drawString(
                    xi + 10,
                    yi_details,
                    f"- {item.filename} has been detected {item.times}",
                )
                yi_details -= 20

            # last table
            canva.showPage()

            table = Table(
                [["Advertisement", "Radio Station", "Detection Datetime", "Timezone"]]
                + [
                    (
                        detection.filename,
                        detection.radio_station_name,
                        to_timezone(detection.detection_date, detection.timezone),
                        detection.timezone,
                    )
                    for detection in detections
                ]
            )
            table.wrapOn(canva, 0, 0)
            table.drawOn(canva, xi + 10, yi - 100)

        else:
            canva.drawString(10, 10, "There are not detection yet.")

        canva.save()

        return FileResponse(self.temp_file.name, media_type="application/pdf")

    async def delete_file(self):
        self.temp_file.close()
