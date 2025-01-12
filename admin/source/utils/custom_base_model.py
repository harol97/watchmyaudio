from humps import camelize
from pydantic import BaseModel


def alias_generator(field: str):
    return camelize(field)


class CustomBaseModel(BaseModel):
    model_config = {
        "populate_by_name": True,
        "from_attributes": True,
        "alias_generator": alias_generator,
    }
