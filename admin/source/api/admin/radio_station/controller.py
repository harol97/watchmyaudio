from typing import Annotated

from fastapi import Body
from pydantic import HttpUrl

from ...admin.client.depends import ClientDepends
from ..user.depends import UserDepends
from .depends import ServiceDepends


class Controller:
    async def create(
        self,
        service: ServiceDepends,
        url: Annotated[HttpUrl, Body(embed=True)],
        user: UserDepends,
    ):
        return await service.create(url, user)

    async def delete(self, service: ServiceDepends, radio_station_id: int):
        radio_station = await service.get_by_id(radio_station_id)
        return await service.delete(radio_station)
