from typing import Annotated

from fastapi import Body
from pydantic import HttpUrl

from ..user.depends import UserDepends
from .depends import ServiceDepends


class Controller:
    async def create(
        self,
        service: ServiceDepends,
        url: Annotated[HttpUrl, Body(embed=True)],
        name: Annotated[str, Body(embed=True)],
        user: UserDepends,
    ):
        return await service.create(url, name, user)

    async def delete(self, service: ServiceDepends, radio_station_id: int):
        radio_station = await service.get_by_id(radio_station_id)
        await service.delete(radio_station)
        return {}

    async def getAll(self, service: ServiceDepends):
        results = await service.get_all()
        return results
