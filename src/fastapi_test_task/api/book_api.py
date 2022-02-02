from fastapi import APIRouter, Depends
from typing import List

from repositories.book_repository import BookRepository, BookRepositoryCreate, BookRepositoryUpdate
from services.book_service import BookService
from api.auth import oauth2_scheme, is_token_valid


router = APIRouter(
    prefix='/books'
)


@router.get('/', response_model=List[BookRepository])
def get_books(
    service: BookService = Depends(), 
    token: str = Depends(oauth2_scheme)
):
    if is_token_valid(token):
        return service.get_all()


@router.get('/{book_id}', response_model=BookRepository)
def get_book(
    book_id: int,
    service: BookService = Depends(),
    token: str = Depends(oauth2_scheme)
):
    if is_token_valid(token):
        return service.get(book_id)


@router.post('/', response_model=BookRepository)
def create_book(
    book_data: BookRepositoryCreate,
    service: BookService = Depends(),
    token: str = Depends(oauth2_scheme)
):
    if is_token_valid(token):
        return service.create(book_data)


@router.put('/{book_id}', response_model=BookRepository)
def update_book(
    book_id: int,
    book_data: BookRepositoryUpdate,
    service: BookService = Depends(),
    token: str = Depends(oauth2_scheme)
):
    if is_token_valid(token):
        return service.update(book_id, book_data)
    

@router.delete('/{book_id}')
def delete_book(
    book_id: int,
    service: BookService = Depends(),
    token: str = Depends(oauth2_scheme)
):
    if is_token_valid(token):
        return service.delete(book_id)
