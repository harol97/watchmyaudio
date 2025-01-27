from datetime import datetime, timedelta, timezone
from typing import Annotated, cast

import jwt
from fastapi import Depends, Header, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

SECRET_KEY = "addassadsad"
ALGORITHM = "HS256"
TOKEN_MINUTES_DURATION = 5000000


class AuthData(BaseModel):
    user_id: int
    exp: datetime | None = None
    is_admin: bool


def create_access_token(data: AuthData, expires_delta: timedelta | None = None) -> str:
    to_encode = data.model_dump()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_MINUTES_DURATION)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(cast(dict, to_encode), SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/admins/auth/login")


def get_token(
    token: Annotated[str, Header()],
) -> AuthData:
    credentials_exception = HTTPException(status.HTTP_401_UNAUTHORIZED)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        data = AuthData.model_validate(payload)
        return data
    except jwt.InvalidTokenError:
        raise credentials_exception


AuthDataDepends = Annotated[AuthData, Depends(get_token)]
