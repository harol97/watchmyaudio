from datetime import datetime
from typing import Annotated
from uuid import uuid4

from pydantic import Field

from source.utils.custom_base_model import CustomBaseModel


def generate_randome_name():
    return str(uuid4())


class AdvertisementIn(CustomBaseModel):
    name: Annotated[str, Field(default_factory=generate_randome_name)]
    radio_stations_ids: list[int]
    start_date: datetime | None
    end_date: datetime | None
    filename_in_system: str


class Advertisement(CustomBaseModel):
    advertisement_id: Annotated[int, Field(alias="id")]
    filename: str
    filename_in_system: str
