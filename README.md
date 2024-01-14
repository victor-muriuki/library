# Library Management System

This project is a simple command-line based library management system implemented in Python. It allows you to manage users, books, and track borrowed books.

## Prerequisites

Make sure you have Python and Pipenv installed on your machine.
     pip install pipenv

# Installation

Clone the repository: 
     git clone <git@github.com:victor-muriuki/library.git>
     cd library

Create a virtual environment and install dependencies:
     pipenv install


# Usage

## Adding Users

    pipenv run python library_cli.py add-user <USER_NAME>

## Adding Books

    pipenv run python library_cli.py add-book <BOOK_TITLE>

## Listing Users

    pipenv run python library_cli.py list-users

## Listing Books

    pipenv run python library_cli.py list-books

## Borrowing a Book

    pipenv run python library_cli.py borrow-book <USER_ID><BOOK_ID>

Replace <USER_ID> and <BOOK_ID> with the actual IDs of the user and book you want to borrow, i.e <1> <4>

## isting Borrowed Books

    pipenv run python library_cli.py list-borrowed-books

# License

This project is licensed under the MIT License - see the LICENSE file for details.






