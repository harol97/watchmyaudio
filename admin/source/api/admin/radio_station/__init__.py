from fastapi import APIRouter

from .controller import Controller
from .dtos import RadioStation

radio_station_router = APIRouter(prefix="/radio_stations", tags=["RadioStation"])

controller = Controller()

radio_station_router.add_api_route(
    "/{radio_station_id}", controller.delete, methods=["DELETE"]
)
radio_station_router.add_api_route(
    "", controller.create, methods=["POST"], response_model=RadioStation
)
