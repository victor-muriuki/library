# models.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    borrowed_books = relationship("BorrowedBook", back_populates="user")

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    borrowed_books = relationship("BorrowedBook", back_populates="book")

class BorrowedBook(Base):
    __tablename__ = 'borrowed_books'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))

    # Define relationships
    user = relationship("User", back_populates="borrowed_books")
    book = relationship("Book", back_populates="borrowed_books")


User.borrowed_books = relationship('BorrowedBook', back_populates='user')
Book.borrowed_books = relationship('BorrowedBook', back_populates='book')
