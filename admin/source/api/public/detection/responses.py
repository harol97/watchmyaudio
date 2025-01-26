from fastapi.responses import FileResponse

from source.utils.custom_base_model import CustomBaseModel


class GetReportResponse(FileResponse):
    media_type = "text/csv"


class GetDataResponse(CustomBaseModel):
    song: str
    data_per_month: list[int]
    color: str
