from datetime import datetime
from typing import Annotated

from pydantic import Field

from source.utils.custom_base_model import CustomBaseModel


class AdvertisementIn(CustomBaseModel):
    name: str
    radio_stations_ids: list[int]
    start_date: datetime | None
    end_date: datetime | None


class Advertisement(CustomBaseModel):
    advertisement_id: Annotated[int, Field(alias="id")]
    filename: str
