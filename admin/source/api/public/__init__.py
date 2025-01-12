from fastapi import APIRouter, Depends

from ..admin.client.depends import get_current_client
from .advertisement import advertisement_router
from .auth import auth_router

public_router = APIRouter(prefix="/public")

public_router.include_router(
    advertisement_router, dependencies=[Depends(get_current_client)]
)
public_router.include_router(auth_router)
public_router.add_api_route(
    "/clients/me", get_current_client, methods=["GET"], tags=["Client"]
)
