from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine

from ..setting import setting

engine = create_engine(setting.url)


def get_session():
    with Session(engine) as session:
        yield session


SessionDepends = Annotated[Session, Depends(get_session)]
