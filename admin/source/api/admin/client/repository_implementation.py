from dataclasses import dataclass
from typing import Sequence

from sqlmodel import select, true

from .model import ClientModel
from .repository import ClientModelUpdate, ClientRepository


@dataclass
class ClientRepositoryImplementaion(ClientRepository):
    async def get_active_all(self) -> Sequence[ClientModel]:
        return self.session.exec(
            select(ClientModel).where(ClientModel.active == true())
        ).all()

    async def get_by_email(self, email: str) -> ClientModel | None:
        return self.session.exec(
            select(ClientModel).where(ClientModel.email == email)
        ).first()

    async def get_active_by_email(self, email: str) -> ClientModel | None:
        return self.session.exec(
            select(ClientModel).where(
                ClientModel.email == email, ClientModel.active == true()
            )
        ).first()

    async def get_by_id(self, client_id: int) -> ClientModel | None:
        return self.session.exec(
            select(ClientModel).where(ClientModel.client_id == client_id)
        ).first()

    async def create(self, new_client: ClientModel):
        self.session.add(new_client)
        self.session.flush()
        return new_client

    async def update(
        self, new_client: ClientModelUpdate, old_client: ClientModel
    ) -> ClientModel:
        old_client.sqlmodel_update(
            new_client.model_dump(exclude_none=True, exclude={"radio_station"})
        )
        self.session.add(old_client)
        if new_client.radio_stations is not None:
            old_client.radio_stations = new_client.radio_stations
        self.session.flush()
        return old_client

    async def delete(self, client: ClientModel):
        self.session.delete(client)
