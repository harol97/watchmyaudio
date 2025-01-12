from typing import Sequence

from fastapi import APIRouter

from .controller import Controller
from .dtos import Advertisement

advertisement_router = APIRouter(prefix="/advertisements", tags=["Advertisement"])

controller = Controller()

advertisement_router.add_api_route(
    "/{advertisement_id}", controller.delete, methods=["DELETE"]
)
advertisement_router.add_api_route(
    "", controller.create, methods=["POST"], response_model=Advertisement
)
advertisement_router.add_api_route(
    "",
    controller.get_by_client,
    methods=["GET"],
    response_model=Sequence[Advertisement],
)
