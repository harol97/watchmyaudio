from fastapi.responses import FileResponse


class GetReportResponse(FileResponse):
    media_type = "text/csv"
