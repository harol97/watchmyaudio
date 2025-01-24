from abc import ABC, abstractmethod

from fastapi.responses import FileResponse

from .dtos import Report


class ReportFileGenerator(ABC):
    @abstractmethod
    async def generate_reportfile(self, detections: list[Report]) -> FileResponse:
        raise NotImplementedError()

    @abstractmethod
    async def delete_file(self): ...
