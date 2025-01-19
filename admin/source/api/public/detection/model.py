from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Column, Field, Integer, Relationship, SQLModel

if TYPE_CHECKING:
    from ...admin.client.model import ClientModel
    from ...admin.radio_station.model import RadioStationModel
    from ..advertisement.model import AdvertisementModel


class Detection(SQLModel, table=True):
    __tablename__ = "detection"  # type: ignore

    detection_id: int | None = Field(
        default=None,
        alias="id",
        sa_column=Column(Integer, name="id", primary_key=True, autoincrement=True),
    )
    datetime_utc: datetime
    advertisement_id: int = Field(foreign_key="advertisement.id")
    radio_station_id: int = Field(foreign_key="radio_station.id")
    client_id: int = Field(foreign_key="client.id")
    timezone: str

    client: "ClientModel" = Relationship()
    radio_station: "RadioStationModel" = Relationship()
    advertisement: "AdvertisementModel" = Relationship()
