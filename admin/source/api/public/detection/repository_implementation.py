from dataclasses import dataclass
from typing import Sequence

from sqlmodel import Session, select

from .model import Detection
from .repository import Repository


@dataclass
class RepositoryImplementation(Repository):
    session: Session

    async def get_detections_by_client(self, client_id: int) -> Sequence[Detection]:
        return self.session.exec(
            select(Detection).where(Detection.client_id == client_id)
        ).all()
