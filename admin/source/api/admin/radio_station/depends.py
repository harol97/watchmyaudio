from typing import Annotated

from fastapi import Depends

from source.dependencies.session import SessionDepends

from .repository import Repository
from .repository_implementation import RepositoryImplementation
from .service import Service
from .service_implementation import ServiceImplementation


def get_repository(session: SessionDepends) -> Repository:
    return RepositoryImplementation(session)


def get_service(
    repository: Annotated[Repository, Depends(get_repository)],
) -> Service:
    return ServiceImplementation(repository)


ServiceDepends = Annotated[Service, Depends(get_service)]
