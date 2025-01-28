from sqlmodel import Column, Field, Integer, SQLModel


class AdvertisementModel(SQLModel, table=True):
    __tablename__ = "advertisement"  # type: ignore
    advertisement_id: int | None = Field(
        default=None,
        alias="id",
        sa_column=Column(Integer, name="id", primary_key=True, autoincrement=True),
    )
    name: str
    filename: str
    filename_in_system: str
    active: bool = Field(default=True)
    client_id: int = Field(foreign_key="client.id", ondelete="CASCADE")
