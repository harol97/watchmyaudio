from typing import TYPE_CHECKING, Literal

from pydantic import HttpUrl
from sqlmodel import Column, Field, Integer, Relationship, SQLModel

from source.utils.database_helpers import HttpUrlType

from ..client_radio_station.model import ClienRadioStationModel

if TYPE_CHECKING:
    from ..radio_station.model import RadioStationModel

ClientKind = Literal["UNDEFINED", "SCHEDULE"]


class ClientModel(SQLModel, table=True):
    __tablename__ = "client"  # type: ignore

    client_id: int | None = Field(
        default=None,
        alias="id",
        sa_column=Column(Integer, name="id", primary_key=True, autoincrement=True),
    )
    name: str
    email: str = Field(unique=True)
    kind: str
    password: str
    phone: str | None = None
    web: HttpUrl | None = Field(default=None, sa_type=HttpUrlType)
    language: str
    active: bool = Field(default=True)
    radio_stations: list["RadioStationModel"] = Relationship(
        back_populates="clients", link_model=ClienRadioStationModel
    )

    @property
    def radio_station_ids(self):
        return [radio_station.radio_station_id for radio_station in self.radio_stations]
