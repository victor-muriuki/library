# cli/list_commands.py
import argparse

def create_subparser(subparsers):
    subparsers.add_parser("list_books", help="List all books")

def execute(args):
    # Implementation for listing all books
    print("Listing all books")
    # Add more logic here
