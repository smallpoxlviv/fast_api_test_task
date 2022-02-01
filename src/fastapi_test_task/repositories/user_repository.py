from pydantic import BaseModel


class UserRepositoryBase(BaseModel):
    first_name: str
    last_name: str

class UserRepository(UserRepositoryBase):
    id: int

    class Config:
        orm_mode = True

class UserRepositoryCreate(UserRepositoryBase):
    pass

class UserRepositoryUpdate(UserRepositoryBase):
    pass