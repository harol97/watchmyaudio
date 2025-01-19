from dataclasses import dataclass
from datetime import datetime
from typing import Sequence

from sqlmodel import Session, select

from .model import Detection
from .repository import Repository


@dataclass
class RepositoryImplementation(Repository):
    session: Session

    async def get_detections_by_client(
        self, client_id: int, start_date: datetime, end_date: datetime
    ) -> Sequence[Detection]:
        return self.session.exec(
            select(Detection).where(
                Detection.client_id == client_id,
                Detection.datetime_utc >= start_date,
                Detection.datetime_utc <= end_date,
            )
        ).all()
