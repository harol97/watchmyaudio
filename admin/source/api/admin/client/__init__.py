from fastapi import APIRouter

from ...public.advertisement.dtos import Advertisement
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
    "/{client_id}", controller.delete, methods=["DELETE"], response_model=None
)

client_router.add_api_route(
    "", controller.get_all, methods=["GET"], response_model=list[Client]
)

client_router.add_api_route(
    "/{client_id}/advertisements",
    controller.get_advertimsements,
    methods=["GET"],
    response_model=list[Advertisement],
)

client_router.add_api_route(
    "/{client_id}", controller.get_by_id, methods=["GET"], response_model=Client
)
