import click
from library.models import Book, BorrowedBook, User
from library.database import SessionLocal, init_db

init_db()

def bubble_sort_books(books):
    n = len(books)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if books[j].title > books[j + 1].title:
                # Swap if the element found is greater
                books[j], books[j + 1] = books[j + 1], books[j]

@click.group()
def cli():
    pass

@cli.command()
@click.argument('title')
def add_book(title):
    book = Book(title=title, available_copies=1)  # Assuming 1 copy for simplicity
    with SessionLocal() as db:
        db.add(book)
        db.commit()
    click.echo(f"Book '{title}' added successfully.")

@cli.command()
def list_books():
    with SessionLocal() as db:
        # Use order_by to sort books by title
        books = db.query(Book).order_by(Book.title).all()

        if books:
            click.echo("List of Books:")
            for book in books:
                click.echo(f"Book ID: {book.id}, Title: {book.title}, Copies: {book.available_copies}")
        else:
            click.echo("No books found.")

@cli.command()
def list_users():
    with SessionLocal() as db:
        users = db.query(User).all()
        if users:
            click.echo("List of Users:")
            for user in users:
                click.echo(f"User ID: {user.id}, Name: {user.name}")
        else:
            click.echo("No users found.")

if __name__ == "__main__":
    cli()
