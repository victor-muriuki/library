# library_cli.py

import click
from library.models import Book, BorrowedBook, User
from library.database import SessionLocal, init_db

init_db()

def sort_books(books):
    # Sort a list of books alphabetically by title
    return sorted(books, key=lambda book: book.title)

def sort_users(users):
    # Sort a list of users alphabetically by name
    return sorted(users, key=lambda user: user.name)


@click.group()
def cli():
    # Define the main click group for the CLI
    pass

@cli.command()
@click.argument('name')
def add_user(name):
    """Add a new user to the library."""
    # Command to add a new user to the library
    user = User(name=name)
    with SessionLocal() as db:
        db.add(user)
        db.commit()
    click.echo(f"User '{name}' added successfully.")

@cli.command()
@click.argument('title')
def add_book(title):
    """Add a new book to the library."""
    # Command to add a new book to the library
    book = Book(title=title)
    with SessionLocal() as db:
        db.add(book)
        db.commit()
    click.echo(f"Book '{title}' added successfully.")

@cli.command()
@click.argument('user_id', type=int)
@click.argument('book_id', type=int)
def borrow_book(user_id, book_id):
    """Borrow a book."""
    with SessionLocal() as db:
        borrow_book(db, user_id, book_id)

def borrow_book(session, user_id, book_id):
    try:
        # Create a new borrowed book entry
        borrowed_book = BorrowedBook(user_id=user_id, book_id=book_id)
        session.add(borrowed_book)
        session.commit()

        click.echo(f"Book borrowed successfully.")
    except NoResultFound:
        click.echo("Error: Book not found.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")
        session.rollback()

@cli.command()
def list_users():
    """List all users in the library."""
    # Command to list all users in the library
    with SessionLocal() as db:
        users = db.query(User).all()

        # Sort the users alphabetically
        sorted_users = sort_users(users)

        if sorted_users:
            click.echo("List of Users:")
            for user in sorted_users:
                click.echo(f"User ID: {user.id}, Name: {user.name}")
        else:
            click.echo("No users found.")

@cli.command()
def list_books():
    """List all books in the library."""
    # Command to list all books in the library
    with SessionLocal() as db:
        books = db.query(Book).all()

        # Sort the books alphabetically
        sorted_books = sort_books(books)

        if sorted_books:
            click.echo("List of Books:")
            for book in sorted_books:
                click.echo(f"Book ID: {book.id}, Title: {book.title}")
        else:
            click.echo("No books found.")

@cli.command()
def list_borrowed_books():
    """List all borrowed books in the library."""
    # Command to list all borrowed books in the library
    with SessionLocal() as db:
        borrowed_books = db.query(BorrowedBook).all()

        if borrowed_books:
            click.echo("List of Borrowed Books:")
            for borrowed_book in borrowed_books:
                click.echo(f"Book ID: {borrowed_book.book_id}, User ID: {borrowed_book.user_id}")
        else:
            click.echo("No borrowed books found.")


# Additional commands (borrow, return) can be added as needed
def return_book(session, user_id, book_id):
    borrowed_book = session.query(BorrowedBook).filter_by(user_id=user_id, book_id=book_id).first()
    if borrowed_book:
        try:
            session.delete(borrowed_book)
            # No need to increment available copies since it's removed from the model
            session.commit()
            click.echo("Book returned successfully.")
        except IntegrityError:
            session.rollback()
            click.echo("Error: Unable to return the book.")
    else:
        click.echo("Borrowed book not found.")

if __name__ == "__main__":
    cli()
