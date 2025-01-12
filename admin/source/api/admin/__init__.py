from fastapi import APIRouter, Depends

from source.api.admin.user.depends import get_current_user_admin

from .auth import auth_router
from .client import client_router
from .radio_station import radio_station_router
from .user import user_router

admin_router = APIRouter(prefix="/admins")

admin_router.include_router(auth_router, dependencies=None)
admin_router.include_router(
    client_router, dependencies=[Depends(get_current_user_admin)]
)
admin_router.include_router(
    radio_station_router, dependencies=[Depends(get_current_user_admin)]
)
admin_router.include_router(user_router, dependencies=[Depends(get_current_user_admin)])
