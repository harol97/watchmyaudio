from fastapi import APIRouter, Depends

from source.api.admin.client.depends import get_current_client

from .controller import Controller
from .responses import GetReportResponse

detection_router = APIRouter(
    prefix="/detections",
    tags=["Detections"],
    dependencies=[Depends(get_current_client)],
)

controller = Controller()

detection_router.add_api_route(
    "/reports", controller.get_report, methods=["GET"], response_class=GetReportResponse
)
