from typing import Sequence, cast

from fastapi import HTTPException, status
from pydantic.type_adapter import TypeAdapter

from source.utils.password import generate, verify
from source.utils.scheduler import Scheduler

from ...public.analyzer.repository import Repository as AnalyzerRepository
from ..client.repository import ClientModelUpdate
from .dtos import Client, ClientIn, UpdateBody
from .model import ClientModel
from .repository import ClientRepository
from .service import Service


class ServiceImplementation(Service):
    def __init__(
        self,
        repository: ClientRepository,
        analyzer_repository: AnalyzerRepository,
    ) -> None:
        self.repository = repository
        self.analyzer_repository = analyzer_repository

    async def create(self, new_client: ClientIn):
        old_client = await self.repository.get_by_email(new_client.email)
        if old_client:
            raise HTTPException(status.HTTP_409_CONFLICT)
        new_client.password = generate(new_client.password)
        client = ClientModel.model_validate(new_client)
        client_created = await self.repository.create(client)
        self.repository.commit()
        return Client.model_validate(client_created)

    async def update(self, data: UpdateBody, client_id: int) -> Client:
        client = await self.repository.get_by_id(client_id)
        if data.password:
            data.password = generate(data.password)
        if not client:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        client_updated = await self.repository.update(
            ClientModelUpdate(**data.model_dump(exclude_none=True)), client
        )
        self.repository.commit()
        return Client.model_validate(client_updated)

    async def get_active_all(self) -> Sequence[Client]:
        clients_models = await self.repository.get_active_all()
        return TypeAdapter(Sequence[Client]).validate_python(clients_models)

    async def get_by_id(self, client_id: int) -> Client:
        client = await self.repository.get_by_id(client_id)
        if not client:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return Client(**client.model_dump())

    async def get_by_email(self, email: str) -> Client:
        client = await self.repository.get_by_email(email)
        if not client:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return Client.model_validate(client)

    async def valid_account(self, email: str, password: str) -> Client:
        client = await self.repository.get_active_by_email(email)
        if not client:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        is_trust_password = verify(password, client.password)
        if not is_trust_password:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)
        return Client(**client.model_dump())

    async def delete(self, client_id: int):
        client = await self.repository.get_by_id(client_id)
        if not client:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        await self.repository.update(ClientModelUpdate(active=False), client)
        analyzers = await self.analyzer_repository.get_by_client(client_id)
        self.repository.commit()
        scheduler = Scheduler.get_instance()
        for analyzer in analyzers:
            scheduler.delete_job(analyzer.job_id)
