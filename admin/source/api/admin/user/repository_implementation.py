from dataclasses import dataclass
from typing import Sequence

from sqlmodel import select

from .model import UserModel
from .repository import UserModelUpdate, UserRepository


@dataclass
class UserRepositoryImplementaion(UserRepository):
    async def get_all(self) -> Sequence[UserModel]:
        return self.session.exec(select(UserModel)).all()

    async def get_by_email(self, email: str) -> UserModel | None:
        return self.session.exec(
            select(UserModel).where(UserModel.email == email)
        ).first()

    async def get_by_id(self, user_id: int) -> UserModel | None:
        return self.session.exec(
            select(UserModel).where(UserModel.user_id == user_id)
        ).first()

    async def create(self, new_user: UserModel):
        self.session.add(new_user)
        self.session.flush()

    async def update(self, new_user: UserModelUpdate, old_user: UserModel) -> UserModel:
        old_user.sqlmodel_update(new_user.model_dump(exclude_none=True))
        self.session.add(old_user)
        self.session.refresh(old_user)
        return old_user

    async def delete(self, user: UserModel):
        self.session.delete(user)
