from fastapi import APIRouter, Depends

from source.api.admin.client.depends import get_current_client

from .controller import Controller
from .responses import GetDataResponse, GetReportResponse

detection_router = APIRouter(
    prefix="/detections",
    tags=["Detections"],
    dependencies=[Depends(get_current_client)],
)

controller = Controller()

detection_router.add_api_route(
    "/reports", controller.get_report, methods=["GET"], response_class=GetReportResponse
)

detection_router.add_api_route(
    "/data",
    controller.get_data,
    methods=["GET"],
    response_model=list[GetDataResponse],
)
