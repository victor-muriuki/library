import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from library.models import User, Book, BorrowedBook, Base

def create_database():
    engine = create_engine('sqlite:///library.db')
    Base.metadata.create_all(engine)
    return engine

def add_user(session, name):
    user = User(name=name)
    session.add(user)
    session.commit()

def add_book(session, title):
    book = Book(title=title)
    session.add(book)
    session.commit()

def list_users(session):
    users = session.query(User).all()
    for user in users:
        print(f"User ID: {user.id}, Name: {user.name}")

def list_books(session):
    books = session.query(Book).all()
    for book in books:
        print(f"Book ID: {book.id}, Title: {book.title}")

def list_borrowed_books(session):
    borrowed_books = session.query(BorrowedBook).all()
    for borrowed_book in borrowed_books:
        print(f"User: {borrowed_book.user.name}, Book: {borrowed_book.book.title}")

def borrow_book(session, user_id, book_id):
    borrowed_book = BorrowedBook(user_id=user_id, book_id=book_id)
    session.add(borrowed_book)
    session.commit()

def return_book(session, user_id, book_id):
    borrowed_book = session.query(BorrowedBook).filter_by(user_id=user_id, book_id=book_id).first()
    if borrowed_book:
        session.delete(borrowed_book)
        session.commit()
        print("Book returned successfully.")
    else:
        print("Borrowed book not found.")

def main():
    engine = create_database()
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        print("\nLibrary CLI Menu:")
        print("1. Add User")
        print("2. Add Book")
        print("3. List Users")
        print("4. List Books")
        print("5. List Borrowed Books")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter user name: ")
            add_user(session, name)
        elif choice == '2':
            title = input("Enter book title: ")
            add_book(session, title)
        elif choice == '3':
            list_users(session)
        elif choice == '4':
            list_books(session)
        elif choice == '5':
            list_borrowed_books(session)
        elif choice == '6':
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID: ")
            borrow_book(session, user_id, book_id)
        elif choice == '7':
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID: ")
            return_book(session, user_id, book_id)
        elif choice == '8':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
