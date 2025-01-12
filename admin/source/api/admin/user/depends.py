from typing import Annotated

from fastapi import Depends, HTTPException, status

from source.dependencies.session import SessionDepends
from source.utils.token import AuthDataDepends

from .dtos import User
from .repository import UserRepository
from .repository_implementation import UserRepositoryImplementaion
from .service import Service
from .service_implementation import ServiceImplementation


def get_repository(session: SessionDepends) -> UserRepository:
    return UserRepositoryImplementaion(session)


UserRepositoryDepends = Annotated[UserRepository, Depends(get_repository)]


def get_service(repository: UserRepositoryDepends) -> Service:
    return ServiceImplementation(repository)


ServiceDepends = Annotated[Service, Depends(get_service)]


async def get_current_user_admin(
    admin_token: AuthDataDepends, repository: UserRepositoryDepends
) -> User:
    credentials_exception = HTTPException(status.HTTP_401_UNAUTHORIZED)
    if not admin_token.is_admin:
        raise credentials_exception
    user = await repository.get_by_id(admin_token.user_id)
    if not user:
        raise credentials_exception
    return User(**user.model_dump())


UserDepends = Annotated[User, Depends(get_current_user_admin)]
