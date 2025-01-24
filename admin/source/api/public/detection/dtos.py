from datetime import datetime
from typing import Annotated

from pydantic import Field, computed_field

from source.utils.custom_base_model import CustomBaseModel
from source.utils.timezone_utlis import to_utc


class Report(CustomBaseModel):
    client_name: str
    radio_station_name: str
    filename: str
    advertisement_id: int
    detection_date: datetime
    timezone: str


class GetReportQuery(CustomBaseModel):
    start_date: Annotated[datetime, Field(alias="startDate")]
    end_date: Annotated[datetime, Field(alias="endDate")]
    timezone: str

    @computed_field
    @property
    def start_date_utc(self) -> datetime:
        return to_utc(self.start_date, self.timezone)

    @computed_field
    @property
    def end_date_utc(self) -> datetime:
        return to_utc(self.end_date, self.timezone)
