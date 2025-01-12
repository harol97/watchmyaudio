from typing import Sequence, cast

from fastapi import HTTPException, status
from pydantic.type_adapter import TypeAdapter
from sqlmodel import delete

from source.utils.password import generate, verify

from ..user.repository import UserModelUpdate
from .dtos import UpdateBody, User, UserIn
from .model import UserModel
from .repository import UserRepository
from .service import Service


class ServiceImplementation(Service):
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    async def create(self, new_user: UserIn) -> User:
        old_user = await self.repository.get_by_email(new_user.email)
        if old_user:
            raise HTTPException(status.HTTP_409_CONFLICT)
        new_user.password = generate(new_user.password)
        user = UserModel.model_validate(new_user)
        await self.repository.create(user)
        self.repository.commit()
        return User.model_validate(user)

    async def update(self, data: UpdateBody, user_id: int) -> User:
        user = await self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        user_updated = await self.repository.update(
            UserModelUpdate(**data.model_dump(exclude_none=True)), user
        )
        self.repository.commit()
        return User(**user_updated.model_dump())

    async def get_by_email(self, email: str) -> User:
        user = await self.repository.get_by_email(email)
        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return User.model_validate(user)

    async def get_all(self) -> Sequence[User]:
        users_models = await self.repository.get_all()
        return TypeAdapter(Sequence[User]).validate_python(users_models)

    async def get_by_id(self, user_id: int) -> User:
        user = await self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return User(**user.model_dump())

    async def valid_account(self, email: str, password: str) -> User:
        user = await self.repository.get_by_email(email)
        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        is_trust_password = verify(password, user.password)
        if not is_trust_password:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)
        return User(**user.model_dump())

    async def delete(self, user_id: int):
        user = cast(UserModel, self.repository.get_by_id(user_id))
        await self.repository.delete(user)
        self.repository.commit()
