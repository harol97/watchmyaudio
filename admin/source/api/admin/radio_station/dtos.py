from typing import Annotated

from pydantic import Field, HttpUrl

from source.utils.custom_base_model import CustomBaseModel


class RadioStation(CustomBaseModel):
    radio_station_id: Annotated[int, Field(alias="id")]
    url: HttpUrl
    name: str
