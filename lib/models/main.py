# main.py (CLI)
import argparse
from cli.book_commands import add_book, borrow_book, return_book, list_books

def main():
    parser = argparse.ArgumentParser(description="Library Management CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subcommands
    add_book.create_subparser(subparsers)
    borrow_book.create_subparser(subparsers)
    return_book.create_subparser(subparsers)
    list_books.create_subparser(subparsers)

    args = parser.parse_args()

    if args.command == "add_book":
        add_book.execute(args)
    elif args.command == "borrow_book":
        borrow_book.execute(args)
    elif args.command == "return_book":
        return_book.execute(args)
    elif args.command == "list_books":
        list_books.execute(args)

if __name__ == "__main__":
    main()
