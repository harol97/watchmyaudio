from abc import ABC, abstractmethod

from ...admin.client.dtos import Client
from .dtos import Report


class Service(ABC):
    @abstractmethod
    async def get_report(self, client: Client) -> list[Report]:
        raise NotImplementedError()
