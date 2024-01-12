# library/cli.py

import click
from library.models import Book, BorrowedBook, User
from library.database import SessionLocal, init_db

init_db()

@click.group()
def cli():
    pass

@cli.command()
@click.argument('title')
@click.argument('author')
@click.argument('total_copies', type=int)
def add_book(title, author, total_copies):
    book = Book(title=title, author=author, total_copies=total_copies, available_copies=total_copies)
    db = SessionLocal()
    db.add(book)
    db.commit()
    click.echo(f"Book '{title}' added successfully.")

@cli.command()
@click.argument('user_name')
def add_user(user_name):
    user = User(name=user_name)
    db = SessionLocal()
    db.add(user)
    db.commit()
    click.echo(f"User '{user_name}' added successfully.")

@cli.command()
@click.argument('book_id', type=int)
@click.argument('user_id', type=int)
def borrow_book(book_id, user_id):
    db = SessionLocal()
    book = db.query(Book).filter_by(id=book_id).first()
    user = db.query(User).filter_by(id=user_id).first()

    if book and user and book.available_copies > 0:
        borrowed_book = BorrowedBook(book=book, user=user)
        book.available_copies -= 1
        db.add(borrowed_book)
        db.commit()
        click.echo(f"Book '{book.title}' borrowed by '{user.name}' successfully.")
    elif not book:
        click.echo(f"Book with ID {book_id} not found.")
    elif not user:
        click.echo(f"User with ID {user_id} not found.")
    elif book.available_copies <= 0:
        click.echo(f"All copies of '{book.title}' are currently borrowed.")

@cli.command()
@click.argument('book_id', type=int)
def return_book(book_id):
    db = SessionLocal()
    borrowed_book = db.query(BorrowedBook).filter_by(book_id=book_id, return_date=None).first()

    if borrowed_book:
        borrowed_book.return_date = datetime.utcnow()
        borrowed_book.book.available_copies += 1
        db.commit()
        click.echo(f"Book '{borrowed_book.book.title}' returned successfully.")
    else:
        click.echo(f"No active borrow record found for Book ID {book_id}.")
