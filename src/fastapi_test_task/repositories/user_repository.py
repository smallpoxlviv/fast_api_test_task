from pydantic import BaseModel


class UserRepositoryBase(BaseModel):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class UserRepository(UserRepositoryBase):
    id: int

class UserRepositoryCreate(UserRepositoryBase):
    pass

class UserRepositoryUpdate(UserRepositoryBase):
    pass