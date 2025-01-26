from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Column, Integer, Relationship, SQLModel
from sqlmodel.main import Field

if TYPE_CHECKING:
    from ...admin.client.model import ClientModel
    from ...admin.radio_station.model import RadioStationModel
    from ..advertisement.model import AdvertisementModel


class AnalyzerModel(SQLModel, table=True):
    __tablename__ = "analyzer"  # type: ignore

    analyzer_id: int | None = Field(
        default=None,
        alias="id",
        sa_column=Column(Integer, name="id", primary_key=True, autoincrement=True),
    )
    advertisement_id: int = Field(foreign_key="advertisement.id", ondelete="CASCADE")
    radio_station_id: int = Field(foreign_key="radio_station.id", ondelete="CASCADE")
    client_id: int = Field(foreign_key="client.id", ondelete="CASCADE")
    start_date: datetime
    end_date: datetime | None
    job_id: str

    client: "ClientModel" = Relationship()
    radio_station: "RadioStationModel" = Relationship()
    advertisement: "AdvertisementModel" = Relationship()
