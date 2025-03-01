from typing import Annotated

from fastapi import Depends, HTTPException, status

from source.dependencies.session import SessionDepends
from source.utils.token import AuthDataDepends

from ...public.analyzer.depends import RepositoryDepends as AnalyzerRepositoryDepends
from ..radio_station.depends import RepositoryDepends as RadioStationRepository
from .dtos import Client
from .repository import ClientRepository
from .repository_implementation import ClientRepositoryImplementaion
from .service import Service
from .service_implementation import ServiceImplementation


def get_repository(session: SessionDepends) -> ClientRepository:
    return ClientRepositoryImplementaion(session)


ClientRepositoryDepends = Annotated[ClientRepository, Depends(get_repository)]


def get_service(
    repository: ClientRepositoryDepends,
    analyzer_repository: AnalyzerRepositoryDepends,
    radio_reporitory: RadioStationRepository,
) -> Service:
    return ServiceImplementation(repository, analyzer_repository, radio_reporitory)


ServiceDepends = Annotated[Service, Depends(get_service)]


async def get_current_client(
    admin_token: AuthDataDepends, repository: ClientRepositoryDepends
) -> Client:
    credentials_exception = HTTPException(status.HTTP_401_UNAUTHORIZED)
    if admin_token.is_admin:
        raise credentials_exception
    client = await repository.get_by_id(admin_token.user_id)
    if not client:
        raise credentials_exception
    return Client(**client.model_dump())


ClientDepends = Annotated[Client, Depends(get_current_client)]
