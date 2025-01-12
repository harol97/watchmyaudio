from .depends import ServiceDepends, UserDepends
from .dtos import UpdateBody, UserIn


class Controller:
    async def me(self, user: UserDepends):
        return user

    async def create(self, service: ServiceDepends, new_user: UserIn):
        return await service.create(new_user)

    async def update(self, service: ServiceDepends, body: UpdateBody, user_id: int):
        return await service.update(body, user_id)

    async def get_all(self, service: ServiceDepends):
        return await service.get_all()

    async def get_by_id(self, service: ServiceDepends, user_id: int):
        return await service.get_by_id(user_id)

    async def delete(self, service: ServiceDepends, user_id: int):
        return await service.delete(user_id)
