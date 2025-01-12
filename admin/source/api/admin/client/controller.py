from ...public.advertisement.depends import (
    ServiceDepends as AdvertisementServiceDepends,
)
from .depends import ServiceDepends
from .dtos import ClientIn, UpdateBody


class Controller:
    async def get_advertimsements(
        self,
        service: ServiceDepends,
        advertisement_service: AdvertisementServiceDepends,
        client_id: int,
    ):
        client = await service.get_by_id(client_id)
        return await advertisement_service.get_by_client(client)

    async def create(self, service: ServiceDepends, new_client: ClientIn):
        return await service.create(new_client)

    async def update(self, service: ServiceDepends, body: UpdateBody, client_id: int):
        return await service.update(body, client_id)

    async def get_all(self, service: ServiceDepends):
        return await service.get_all()

    async def get_by_id(self, service: ServiceDepends, client_id: int):
        return await service.get_by_id(client_id)

    async def delete(self, service: ServiceDepends, client_id: int):
        return await service.delete(client_id)
