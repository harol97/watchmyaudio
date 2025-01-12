from typing import Annotated

from fastapi import Depends
from sqlalchemy_utils.functions.database import create_database, database_exists
from sqlmodel import Session, create_engine

url = "sqlite:///database.db"

engine = create_engine(url)

if not database_exists(url):
    create_database(url)


def get_session():
    with Session(engine) as session:
        yield session


SessionDepends = Annotated[Session, Depends(get_session)]
