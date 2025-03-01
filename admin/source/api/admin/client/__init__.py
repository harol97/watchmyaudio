from fastapi import APIRouter

from ...public.advertisement.dtos import Advertisement
from ..radio_station.dtos import RadioStation
from .controller import Controller
from .dtos import Client

client_router = APIRouter(prefix="/clients", tags=["Client"])

controller = Controller()


client_router.add_api_route(
    "", controller.create, methods=["POST"], response_model=Client
)
client_router.add_api_route(
    "/{client_id}", controller.update, methods=["PATCH"], response_model=Client
)


client_router.add_api_route(
    "/{client_id}", controller.delete, methods=["DELETE"], response_model=dict
)

client_router.add_api_route(
    "", controller.get_active_all, methods=["GET"], response_model=list[Client]
)

client_router.add_api_route(
    "/{client_id}/advertisements",
    controller.get_advertimsements,
    methods=["GET"],
    response_model=list[Advertisement],
)

client_router.add_api_route(
    "/{client_id}/radio-stations",
    controller.get_radio_stations,
    methods=["GET"],
    response_model=list[RadioStation],
)

client_router.add_api_route(
    "/{client_id}", controller.get_by_id, methods=["GET"], response_model=Client
)
