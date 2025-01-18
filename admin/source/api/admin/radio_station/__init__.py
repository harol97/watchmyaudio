from typing import Sequence

from fastapi import APIRouter

from .controller import Controller
from .dtos import RadioStation

radio_station_router = APIRouter(prefix="/radio-stations", tags=["RadioStation"])

controller = Controller()

radio_station_router.add_api_route(
    "/{radio_station_id}", controller.delete, methods=["DELETE"], response_model=dict
)
radio_station_router.add_api_route(
    "", controller.create, methods=["POST"], response_model=RadioStation
)
radio_station_router.add_api_route(
    "", controller.getAll, methods=["GET"], response_model=Sequence[RadioStation]
)
