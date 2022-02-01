from fastapi import Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List
from repositories.book_repository import BookRepositoryCreate, BookRepositoryUpdate

from tables import Book
from database import get_session

class BookService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, book_id: int) -> Book:
        book = (
            self.session
            .query(Book)
            .filter_by(id=book_id)
            .first()
        )
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return book 

    def get_all(self) -> List[Book]:
        books = (
            self.session
            .query(Book)
            .all()
        )
        return books

    def get(self, book_id: int) -> Book:
        return self._get(book_id)   

    def create(self, book_data: BookRepositoryCreate) -> Book:
        book = Book(**book_data.dict())
        self.session.add(book)
        self.session.commit()
        return book

    def update(self, book_id: int, book_data: BookRepositoryUpdate):
        book = self._get(book_id)
        for field, value in book_data:
            setattr(book, field, value)
        self.session.commit()
        return book    

    def delete(self, book_id: int):
        book = self._get(book_id)
        self.session.delete(book)
        self.session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)