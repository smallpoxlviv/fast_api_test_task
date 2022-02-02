from pydantic import BaseModel


class BookRepositoryBase(BaseModel):
    title: str
    author: str
    user_id: int = None

class BookRepository(BookRepositoryBase):
    id: int

    class Config:
        orm_mode = True

class BookRepositoryCreate(BookRepositoryBase):
    pass

class BookRepositoryUpdate(BookRepositoryBase):
    pass