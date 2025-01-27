from dataclasses import dataclass
from itertools import groupby
from random import choice
from tempfile import NamedTemporaryFile
from reportlab.graphics.charts.linecharts import HorizontalLineChart

from fastapi.responses import FileResponse
from reportlab.graphics.shapes import Drawing
from reportlab.lib.colors import black
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
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
        doc = SimpleDocTemplate(
            self.temp_file.name,
            pageSize=A4,
            rightMargin=0,
            leftMargin=0,
            topMargin=0,
            bottomMargin=0,
        )
        body = []

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
            space = Spacer(1, 30)
            body.append(Paragraph("Graphic Report Distribution (Bar Chart)"))
            body.append(space)
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
            bc.categoryAxis.categoryNames = (
                "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(" ")
            )
            for index, item in enumerate(items):
                bc.lines[index].strokeColor = item.color.rgb
            drawing = Drawing()
            drawing.add(bc)
            body.append(drawing)
            body.append(space)

            # details
            body.append(Paragraph("Details:"))
            for item in items:
                style = getSampleStyleSheet()["Normal"]
                style.textColor = item.color.rgb
                body.append(
                    Paragraph(
                        f"- {item.filename} has been detected {item.times}", style
                    )
                )
            body.append(space)

            # last table
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
            body.append(table)

        else:
            body.append("There are not detection yet.")

        doc.build(body)
        return FileResponse(self.temp_file.name, media_type="application/pdf")

    async def delete_file(self):
        self.temp_file.close()
