from fastapi import APIRouter, Depends

from ..admin.client.controller import Controller as ClientController
from ..admin.client.depends import get_current_client
from ..admin.radio_station.dtos import RadioStation
from .advertisement import advertisement_router
from .auth import auth_router
from .detection import detection_router

public_router = APIRouter(prefix="/public")

client_controller = ClientController()

public_router.include_router(
    advertisement_router, dependencies=[Depends(get_current_client)]
)
public_router.include_router(auth_router)

public_router.add_api_route(
    "/clients/me", get_current_client, methods=["GET"], tags=["Client"]
)

public_router.add_api_route(
    "/clients/radio-stations",
    client_controller.get_my_radio_stations,
    methods=["GET"],
    tags=["Client"],
    response_model=list[RadioStation],
    dependencies=[Depends(get_current_client)],
)

public_router.include_router(detection_router)
