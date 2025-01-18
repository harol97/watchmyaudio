from abc import ABC, abstractmethod
from typing import Sequence

from .model import Detection


class Repository(ABC):
    @abstractmethod
    async def get_detections_by_client(self, client_id: int) -> Sequence[Detection]:
        raise NotImplementedError()
