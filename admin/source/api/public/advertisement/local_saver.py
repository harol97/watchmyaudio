from typing import BinaryIO

from .save_advertisement import AdvertisementSaver


class LocalSaver(AdvertisementSaver):
    async def save(self, file: BinaryIO, filename: str):
        with open(filename, "wb") as f:
            f.write(file.read())
