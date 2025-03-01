from sqlmodel import Field, SQLModel


class ClienRadioStationModel(SQLModel, table=True):
    __tablename__ = "client_radio_station"  # type: ignore
    client_id: int | None = Field(
        default=None, foreign_key="client.id", primary_key=True
    )
    radio_station_id: int | None = Field(
        default=None, foreign_key="radio_station.id", primary_key=True
    )
