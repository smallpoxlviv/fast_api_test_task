import sqlalchemy as sqla
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    first_name = sqla.Column(sqla.String)
    last_name = sqla.Column(sqla.String)

class Book(Base):
    __tablename__ = 'books'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    title = sqla.Column(sqla.String)
    author = sqla.Column(sqla.String)
    