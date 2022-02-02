from pydantic import BaseModel
import typing
from .book_repository import BookRepository


class UserRepositoryBase(BaseModel):
    first_name: str
    last_name: str

class UserRepository(UserRepositoryBase):
    id: int
    books: typing.List[BookRepository]

    class Config:
        orm_mode = True

class UserRepositoryCreate(UserRepositoryBase):
    pass

class UserRepositoryUpdate(UserRepositoryBase):
    pass