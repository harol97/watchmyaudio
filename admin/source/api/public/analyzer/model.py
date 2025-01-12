from datetime import datetime

from sqlmodel import Column, Integer, SQLModel
from sqlmodel.main import Field


class AnalyzerModel(SQLModel, table=True):
    __tablename__ = "analyzer"  # type: ignore

    analyzer_id: int | None = Field(
        default=None,
        alias="id",
        sa_column=Column(Integer, name="id", primary_key=True, autoincrement=True),
    )
    advertisement_id: int = Field(foreign_key="advertisement.id")
    radio_station_id: int = Field(foreign_key="radio_station.id")
    client_id: int = Field(foreign_key="client.id")
    start_date: datetime
    end_date: datetime | None
    job_id: str
