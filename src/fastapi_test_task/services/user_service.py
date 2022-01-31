from fastapi import Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List
from repositories.user_repository import UserRepositoryCreate, UserRepositoryUpdate

from tables import User
from database import get_session

class UserService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int) -> User:
        user = (
            self.session
            .query(User)
            .filter_by(id=user_id)
            .first()
        )
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return user 

    def get_all(self) -> List[User]:
        users = (
            self.session
            .query(User)
            .all()
        )
        return users

    def get(self, user_id: int) -> User:
        return self._get(user_id)   

    def create(self, user_data: UserRepositoryCreate) -> User:
        user = User(**user_data.dict())
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user_id: int, user_data: UserRepositoryUpdate):
        user = self._get(user_id)
        for field, value in user_data:
            setattr(user, field, value)
        self.session.commit()
        return user    

    def delete(self, user_id: int):
        user = self._get(user_id)
        self.session.delete(user)
        self.session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)