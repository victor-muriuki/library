# import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from library.models import User, Book, BorrowedBook, Base

def create_database():
    engine = create_engine('sqlite:///library.db')
    Base.metadata.create_all(engine)
    return engine

def add_user(session, name):
    try:
        user = User(name=name)
        session.add(user)
        session.commit()
        print("User added successfully.")
    except IntegrityError:
        session.rollback()
        print("Error: User with the same name already exists.")

def add_book(session, title):
    try:
        book = Book(title=title)
        session.add(book)
        session.commit()
        print("Book added successfully.")
    except IntegrityError:
        session.rollback()
        print("Error: Book with the same title already exists.")

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

def list_borrowed_books(session):
    borrowed_books = session.query(BorrowedBook).all()
    if borrowed_books:
        for borrowed_book in borrowed_books:
            user_name = borrowed_book.user.name if borrowed_book.user else "Unknown User"
            book_title = borrowed_book.book.title if borrowed_book.book else "Unknown Book"
            print(f"User: {user_name}, Book: {book_title}")
    else:
        print("No borrowed books found.")






def borrow_book(session, user_id, book_id):
    try:
        borrowed_book = BorrowedBook(user_id=user_id, book_id=book_id)
        session.add(borrowed_book)
        session.commit()
        print("Book borrowed successfully.")
    except IntegrityError:
        session.rollback()
        print("Error: User or Book not found, or the book is already borrowed.")

def return_book(session, user_id, book_id):
    borrowed_book = session.query(BorrowedBook).filter_by(user_id=user_id, book_id=book_id).first()
    if borrowed_book:
        try:
            session.delete(borrowed_book)
            session.commit()
            print("Book returned successfully.")
        except IntegrityError:
            session.rollback()
            print("Error: Unable to return the book.")
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

        try:
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
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
