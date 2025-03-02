from dataclasses import dataclass
from typing import Sequence, cast

from fastapi import HTTPException, status
from pydantic.type_adapter import TypeAdapter
from sqlmodel import col

from source.api.admin.radio_station.model import RadioStationModel
from source.utils.password import generate, verify
from source.utils.scheduler import Scheduler

from ...public.analyzer.repository import Repository as AnalyzerRepository
from ..client.repository import ClientModelUpdate
from ..radio_station.dtos import RadioStation
from ..radio_station.repository import Repository as RadioStationRepository
from .dtos import Client, ClientIn, UpdateBody
from .model import ClientModel
from .repository import ClientRepository
from .service import Service

radio_station_list_adapter = TypeAdapter(list[RadioStation])


@dataclass
class ServiceImplementation(Service):
    repository: ClientRepository
    analyzer_repository: AnalyzerRepository
    radio_station_repository: RadioStationRepository

    async def create(self, new_client: ClientIn):
        old_client = await self.repository.get_by_email(new_client.email)
        if old_client:
            raise HTTPException(status.HTTP_409_CONFLICT)
        new_client.password = generate(new_client.password)
        client = ClientModel.model_validate(
            new_client.model_dump(exclude={"radio_station_ids"})
        )
        client_created = await self.repository.create(client)
        radio_stations = await self.radio_station_repository.get_by_ids(
            new_client.radio_station_ids
        )
        client_created.radio_stations = cast(list, radio_stations)
        self.repository.commit()
        return Client.model_validate(client_created)

    async def update(self, data: UpdateBody, client_id: int) -> Client:
        client = await self.repository.get_by_id(client_id)
        if data.password:
            data.password = generate(data.password)
        if not client:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        model_update = ClientModelUpdate.model_validate(
            data.model_dump(exclude_none=True, exclude={"radio_station_ids"})
        )
        if data.radio_station_ids is not None:
            old_radio_station_ids = set(client.radio_station_ids)
            new_radio_station_ids = set(data.radio_station_ids)
            ids_to_delete = (
                old_radio_station_ids - new_radio_station_ids
            )  # to delete process on schedule
            radio_stations = await self.radio_station_repository.get_by_ids(
                data.radio_station_ids
            )
            model_update.radio_stations = list(radio_stations)
            analyzers = self.analyzer_repository.get(
                [
                    ClientModel.client_id == client.client_id,  # type: ignore
                    col(RadioStationModel.radio_station_id).in_(ids_to_delete),
                ]
            )
            for analyzer in analyzers:
                Scheduler.get_instance().delete_job(analyzer.job_id)

        client_updated = await self.repository.update(
            model_update,
            client,
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

    async def get_radio_stations(self, client_id: int):
        client = await self.repository.get_by_id(client_id)
        if not client:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return radio_station_list_adapter.validate_python(client.radio_stations)
