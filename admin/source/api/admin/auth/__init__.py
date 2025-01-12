from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer

from .controller import Controller
from .dtos import LoginResponse
from .service import Service

controller = Controller(Service())
oauth_schema = OAuth2PasswordBearer(tokenUrl="login")
auth_router = APIRouter(prefix="/auth", tags=["Auth"])

auth_router.add_api_route(
    "/login", controller.login, methods=["POST"], response_model=LoginResponse
)
