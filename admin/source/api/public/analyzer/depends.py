from typing import Annotated

from fastapi import Depends

from source.dependencies.session import SessionDepends

from .repository import Repository


def get_repository(session: SessionDepends):
    return Repository(session)


RepositoryDepends = Annotated[Repository, Depends(get_repository)]
