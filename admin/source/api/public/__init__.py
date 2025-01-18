from fastapi import APIRouter, Depends

from ..admin.client.depends import get_current_client
from ..admin.radio_station.controller import Controller as RadioStationController
from ..admin.radio_station.dtos import RadioStation
from .advertisement import advertisement_router
from .auth import auth_router

public_router = APIRouter(prefix="/public")

radio_station_controller = RadioStationController()

public_router.include_router(
    advertisement_router, dependencies=[Depends(get_current_client)]
)
public_router.include_router(auth_router)

public_router.add_api_route(
    "/clients/me", get_current_client, methods=["GET"], tags=["Client"]
)

public_router.add_api_route(
    "/radio-stations",
    radio_station_controller.getAll,
    methods=["GET"],
    tags=["RadioStation"],
    response_model=list[RadioStation],
    dependencies=[Depends(get_current_client)],
)
