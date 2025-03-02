from typing import TYPE_CHECKING

from sqlmodel import Column, Field, Integer, Relationship, SQLModel

from ..client_radio_station.model import ClienRadioStationModel

if TYPE_CHECKING:
    from ...public.analyzer.model import AnalyzerModel
    from ..client.model import ClientModel


class RadioStationModel(SQLModel, table=True):
    __tablename__ = "radio_station"  # type: ignore

    radio_station_id: int | None = Field(
        default=None,
        sa_column=Column(Integer, name="id", primary_key=True, autoincrement=True),
    )
    url: str
    name: str
    user_id: int = Field(foreign_key="user.id", ondelete="CASCADE")
    clients: list["ClientModel"] = Relationship(
        back_populates="radio_stations", link_model=ClienRadioStationModel
    )
    analyzer: "AnalyzerModel" = Relationship(back_populates="radio_station")
