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


# # main.py (CLI)
# import argparse
# from cli.book_commands import add_book, borrow_book, return_book, list_books

# def main():
#     parser = argparse.ArgumentParser(description="Library Management CLI")
#     subparsers = parser.add_subparsers(dest="command", help="Available commands")

#     # Subcommands
#     add_book.create_subparser(subparsers)
#     borrow_book.create_subparser(subparsers)
#     return_book.create_subparser(subparsers)
#     list_books.create_subparser(subparsers)

#     args = parser.parse_args()

#     if args.command == "add_book":
#         add_book.execute(args)
#     elif args.command == "borrow_book":
#         borrow_book.execute(args)
#     elif args.command == "return_book":
#         return_book.execute(args)
#     elif args.command == "list_books":
#         list_books.execute(args)

# if __name__ == "__main__":
#     main()