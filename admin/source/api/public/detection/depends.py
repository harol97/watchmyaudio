from typing import Annotated

from fastapi import Depends

from source.dependencies.session import SessionDepends

from .pdf_generator import PdfGenerator
from .reportfile_generator import ReportFileGenerator
from .repository import Repository
from .repository_implementation import RepositoryImplementation
from .service import Service
from .service_implementation import ServiceImplementation


def get_repository(session: SessionDepends) -> Repository:
    return RepositoryImplementation(session)


RepositoryDepends = Annotated[Repository, Depends(get_repository)]


def get_service(repository: RepositoryDepends) -> Service:
    return ServiceImplementation(repository)


ServiceDepends = Annotated[Service, Depends(get_service)]


async def get_report_generator():
    generator = PdfGenerator()
    yield generator
    await generator.delete_file()


ReportFileGeneratorDepends = Annotated[
    ReportFileGenerator, Depends(get_report_generator)
]
