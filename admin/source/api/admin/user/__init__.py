from fastapi import APIRouter, Depends

from source.api.admin.user.depends import get_current_user_admin

from .controller import Controller
from .dtos import User

user_router = APIRouter(
    prefix="/users", tags=["User"], dependencies=[Depends(get_current_user_admin)]
)

controller = Controller()

user_router.add_api_route("/me", controller.me, methods=["GET"], response_model=User)
user_router.add_api_route("", controller.create, methods=["POST"], response_model=User)
user_router.add_api_route(
    "/{user_id}", controller.update, methods=["PATCH"], response_model=User
)
user_router.add_api_route(
    "", controller.get_all, methods=["GET"], response_model=list[User]
)
user_router.add_api_route(
    "/{user_id}", controller.get_by_id, methods=["GET"], response_model=User
)

user_router.add_api_route("/{user_id}", controller.delete, methods=["DELETE"])
