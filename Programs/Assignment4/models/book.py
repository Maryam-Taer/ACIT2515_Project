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
        """ Abstract method to borrow book """
        raise NotImplementedError('To be used in special entities')

    def return_book(self, book_id):
        """ Abstract method to return book to library """
        raise NotImplementedError('To be used in special entities')

    def to_dict(self) -> dict:
        """ Return book instance state as a dictionary """
        raise NotImplementedError('To be used in special entities')

    def get_book_type(self) -> None:
        """ Abstract method of the book type -> to be used in child classes """
        raise NotImplementedError('To be used in special entities')
