# Group 16
# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-04-08

"""The program creates a 'Book' object in 'Book' class to display the
book information needed for a customer who needs to borrow a book.
It also provides information on the book availability status; meaning
whether a book has been borrowed already or not"""

from database.database import db
from peewee import Model, CharField, IntegerField, BooleanField


class Book(Model):
    """initiates all the common attributes of a book"""
    MIN_EDITION = 1
    MIN_LENGTH = 3
    MAX_LENGTH = 7
    MIN_PUBLISHED_YEAR = 1920
    MAX_PUBLISHED_YEAR = 2020

    book_id = CharField(unique=True, column_name='book_id')
    book_title = CharField(column_name='title')
    author = CharField(column_name='author')
    published_year = IntegerField(column_name='published')
    edition = IntegerField(column_name='edition')
    is_borrowed = BooleanField(default=False, column_name='is_borrowed')

    class Meta:
        database = db

    def borrow(self, book_id):
        raise NotImplementedError()

    def return_book(self, book_id):
        raise NotImplementedError()

    def to_dict(self) -> dict:
        """returns book instance state as a dictionary"""
        raise NotImplementedError()

    def get_book_type(self) -> None:
        """abstract method of the book type -> to be used in child classes"""
        raise NotImplementedError()

    @classmethod
    def validation(cls, book_id: str, book_title: str, author: str, published_year: int, edition: int) -> None:
        if type(book_id) != str:
            raise TypeError('Invalid book id! PLease enter the right id (e.g. s0124)')
        if len(book_id) < cls.MIN_LENGTH or len(book_id) > cls.MAX_LENGTH:
            raise ValueError('Book id needs to be between 3 to 7 characters.')
        if type(book_title) != str:
            raise TypeError(f'Book with the title {book_title} not found.')
        if type(author) != str:
            raise TypeError(f'No book written by {author} found.')
        if type(published_year) != int:
            raise TypeError('Invalid published year! PLease enter again')
        if published_year < cls.MIN_PUBLISHED_YEAR or published_year > cls.MAX_PUBLISHED_YEAR:
            raise ValueError('Books published between 1995 and 2020 available in the library only.')
        if type(edition) != int:
            raise TypeError('invalid edition type! PLease enter again')
        if edition < cls.MIN_EDITION:
            raise ValueError(f'The edition {edition} of this book does not exist in the library.')
