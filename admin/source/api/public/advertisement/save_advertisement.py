from abc import ABC, abstractmethod
from typing import BinaryIO


class AdvertisementSaver(ABC):
    @abstractmethod
    async def save(self, file: BinaryIO, filename: str): ...
