from abc import ABC, abstractmethod
from datetime import datetime

from ...admin.client.dtos import Client
from .dtos import Report
from .responses import GetDataResponse


class Service(ABC):
    @abstractmethod
    async def get_report(
        self, client: Client, start_date: datetime, end_date: datetime
    ) -> list[Report]:
        raise NotImplementedError()

    @abstractmethod
    async def get_data(
        self, client: Client, start_date: datetime, end_date: datetime
    ) -> list[GetDataResponse]:
        raise NotImplementedError()
