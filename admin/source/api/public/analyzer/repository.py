from typing import Sequence

from sqlmodel import select

from source.utils.base_repository import BaseRepository

from .model import AnalyzerModel


class Repository(BaseRepository):
    def create(self, analyzer: AnalyzerModel) -> AnalyzerModel:
        self.session.add(analyzer)
        self.session.flush()
        return analyzer

    async def get_by_client(self, client_id: int) -> Sequence[AnalyzerModel]:
        return self.session.exec(
            select(AnalyzerModel).where(AnalyzerModel.client_id == client_id)
        ).all()

    async def get_by_advertisement(
        self, advertisement_id: int
    ) -> Sequence[AnalyzerModel]:
        return self.session.exec(
            select(AnalyzerModel).where(
                AnalyzerModel.advertisement_id == advertisement_id
            )
        ).all()

    async def get_by_radio_station(
        self, radio_station_id: int
    ) -> Sequence[AnalyzerModel]:
        return self.session.exec(
            select(AnalyzerModel).where(
                AnalyzerModel.radio_station_id == radio_station_id
            )
        ).all()

    def create_many(self, analyzers: list[AnalyzerModel]) -> list[AnalyzerModel]:
        for analyzer in analyzers:
            self.session.add(analyzer)
        self.session.flush()
        return analyzers
