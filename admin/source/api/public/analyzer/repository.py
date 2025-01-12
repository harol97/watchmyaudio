from source.utils.base_repository import BaseRepository

from .model import AnalyzerModel


class Repository(BaseRepository):
    def create(self, analyzer: AnalyzerModel) -> AnalyzerModel:
        self.session.add(analyzer)
        self.session.flush()
        return analyzer

    def create_many(self, analyzers: list[AnalyzerModel]) -> list[AnalyzerModel]:
        for analyzer in analyzers:
            self.session.add(analyzer)
        self.session.flush()
        return analyzers
