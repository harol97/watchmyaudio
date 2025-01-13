from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine

url = "sqlite:///database.db"

engine = create_engine(url)


def get_session():
    with Session(engine) as session:
        yield session


SessionDepends = Annotated[Session, Depends(get_session)]
