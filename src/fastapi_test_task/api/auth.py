from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status
from settings import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def is_token_valid(token: str):
    if token != settings.super_secret_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": token},
        )
    return True