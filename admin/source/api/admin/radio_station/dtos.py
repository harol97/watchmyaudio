from typing import Annotated

from pydantic import Field, HttpUrl

from source.utils.custom_base_model import CustomBaseModel


class RadioStationIn(CustomBaseModel):
    url: HttpUrl
    name: str


class RadioStation(RadioStationIn):
    radio_station_id: Annotated[int, Field(alias="id")]
    url: HttpUrl
    name: str
