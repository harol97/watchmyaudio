from dataclasses import dataclass

from sqlmodel import Session


@dataclass
class BaseRepository:
    session: Session

    def commit(self):
        self.session.commit()
