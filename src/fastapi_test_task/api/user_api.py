from fastapi import APIRouter, Depends
from typing import List

from repositories.user_repository import UserRepository, UserRepositoryCreate, UserRepositoryUpdate
from services.user_service import UserService
from api.auth import oauth2_scheme, is_token_valid


router = APIRouter(
    prefix='/users'
)


@router.get('/', response_model=List[UserRepository])
def get_users(
    service: UserService = Depends(),
    token: str = Depends(oauth2_scheme)
):
    if is_token_valid(token):
        return service.get_all()


@router.get('/{user_id}', response_model=UserRepository)
def get_user(
    user_id: int,
    service: UserService = Depends(),
    token: str = Depends(oauth2_scheme)
):
    if is_token_valid(token):
        return service.get(user_id)


@router.post('/', response_model=UserRepository)
def create_user(
    user_data: UserRepositoryCreate,
    service: UserService = Depends(),
    token: str = Depends(oauth2_scheme)
):
    if is_token_valid(token):
        return service.create(user_data)


@router.put('/{user_id}', response_model=UserRepository)
def update_user(
    user_id: int,
    user_data: UserRepositoryUpdate,
    service: UserService = Depends(),
    token: str = Depends(oauth2_scheme)
):
    if is_token_valid(token):
        return service.update(user_id, user_data)
    

@router.delete('/{user_id}')
def delete_user(
    user_id: int,
    service: UserService = Depends(),
    token: str = Depends(oauth2_scheme)
):
    if is_token_valid(token):
        return service.delete(user_id)
