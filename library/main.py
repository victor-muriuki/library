# main.py

from sqlalchemy.orm import sessionmaker
from library.models import Book, User, Base
from library_cli import create_database


def list_users(session):
    users = session.query(User).all()
    if users:
        for user in users:
            print(f"User ID: {user.id}, Name: {user.name}")
    else:
        print("No users found.")

def list_books(session):
    books = session.query(Book).all()
    if books:
        for book in books:
            print(f"Book ID: {book.id}, Title: {book.title}")
    else:
        print("No books found.")


if __name__ == "__main__":
    engine = create_database()
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

