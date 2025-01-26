from sqlmodel import Column, Field, Integer, SQLModel


class RadioStationModel(SQLModel, table=True):
    __tablename__ = "radio_station"  # type: ignore

    radio_station_id: int | None = Field(
        default=None,
        sa_column=Column(Integer, name="id", primary_key=True, autoincrement=True),
    )
    url: str
    name: str
    user_id: int = Field(foreign_key="user.id", ondelete="CASCADE")
