from source.utils.custom_base_model import CustomBaseModel


class FilterQuery(CustomBaseModel):
    active: bool


class UpdateQuery(CustomBaseModel):
    active: bool | None = None
