from abc import ABC, abstractmethod
from datetime import datetime
from typing import Sequence

from .model import Detection


class Repository(ABC):
    @abstractmethod
    async def get_detections_by_client(
        self, client_id: int, start_date: datetime, end_date: datetime
    ) -> Sequence[Detection]:
        raise NotImplementedError()
