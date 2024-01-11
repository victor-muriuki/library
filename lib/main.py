# main.py
import argparse
from cli import book_commands, borrow_commands, return_commands, list_commands

def main():
    parser = argparse.ArgumentParser(description="Library Management CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subcommands
    book_commands.create_subparser(subparsers)
    borrow_commands.create_subparser(subparsers)
    return_commands.create_subparser(subparsers)
    list_commands.create_subparser(subparsers)

    args = parser.parse_args()

    if args.command == "add_book":
        book_commands.execute(args)
    elif args.command == "borrow_book":
        borrow_commands.execute(args)
    elif args.command == "return_book":
        return_commands.execute(args)
    elif args.command == "list_books":
        list_commands.execute(args)

if __name__ == "__main__":
    main()
