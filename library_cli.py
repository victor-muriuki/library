import click
from library.models import Book, BorrowedBook, User
from library.database import SessionLocal, init_db

init_db()

def sort_items(items, key_function):
    return sorted(items, key=key_function)

def sort_books(books):
    return sort_items(books, key=lambda book: book.title)

def sort_users(users):
    return sort_items(users, key=lambda user: user.name)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
def add_user(name):
    """Add a new user to the library."""
    user = User(name=name)
    with SessionLocal() as db:
        db.add(user)
        db.commit()
    click.echo(f"User '{name}' added successfully.")

@cli.command()
@click.argument('title')
def add_book(title):
    """Add a new book to the library."""
    book = Book(title=title, available_copies=1)  # Assuming 1 copy for simplicity
    with SessionLocal() as db:
        db.add(book)
        db.commit()
    click.echo(f"Book '{title}' added successfully.")

@cli.command()
def list_users():
    """List all users in the library."""
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
    with SessionLocal() as db:
        books = db.query(Book).all()

        # Sort the books alphabetically
        sorted_books = sort_books(books)

        if sorted_books:
            click.echo("List of Books:")
            for book in sorted_books:
                click.echo(f"Book ID: {book.id}, Title: {book.title}, Copies: {book.available_copies}")
        else:
            click.echo("No books found.")

@cli.command()
def list_borrowed_books():
    """List all borrowed books in the library."""
    with SessionLocal() as db:
        borrowed_books = db.query(BorrowedBook).all()

        if borrowed_books:
            click.echo("List of Borrowed Books:")
            for borrowed_book in borrowed_books:
                click.echo(f"Book ID: {borrowed_book.book_id}, User ID: {borrowed_book.user_id}, Due Date: {borrowed_book.due_date}")
        else:
            click.echo("No borrowed books found.")

# Additional commands (borrow, return) can be added as needed

if __name__ == "__main__":
    cli()
