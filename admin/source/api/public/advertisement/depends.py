from typing import Annotated

from fastapi import Depends

from source.dependencies.session import SessionDepends

from ..analyzer.depends import RepositoryDepends as AnalyzerRepositoryDepends
from .local_saver import LocalSaver
from .repository import Repository
from .repository_implementation import RepositoryImplementation
from .save_advertisement import AdvertisementSaver
from .service import Service
from .service_implementation import ServiceImplementation


def get_file_server() -> AdvertisementSaver:
    return LocalSaver()


FileSaverDepends = Annotated[AdvertisementSaver, Depends(get_file_server)]


def get_repository(session: SessionDepends) -> Repository:
    return RepositoryImplementation(session)


def get_service(
    repository: Annotated[Repository, Depends(get_repository)],
    analyzer_repository: AnalyzerRepositoryDepends,
) -> Service:
    return ServiceImplementation(repository, analyzer_repository)


ServiceDepends = Annotated[Service, Depends(get_service)]
