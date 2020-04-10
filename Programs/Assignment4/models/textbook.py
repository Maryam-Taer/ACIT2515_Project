# Group 16
# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-04-08

"""This is the child class of 'Book' class that inherits common attributes
initiated in the 'Book' class while specifying its own attributes that
distinguishes a 'text book' with other type of books"""

from .book import Book
from peewee import CharField


class Textbook(Book):
    BOOK_TYPE = 'textbook'
    COVER_TYPE = ['paperback', 'hardcover case wrap', 'hardcover dust jacket']
    BOOK_SUBJECT = ['language', 'biology', 'health', 'english', 'french', 'arts',
                    'music', 'science', 'psychology', 'math', 'poetry', 'history',
                    'chemistry', 'physics', 'literature', 'short story']

    """initiates all the special attributes of a book as well as inheriting the common attributes"""
    cover_type = CharField()
    book_subject = CharField()

    def borrow(self, book_id):
        """Set 'is_borrowed' attribute to true"""
        textbook = Textbook.select().where(Textbook.book_id == book_id).get()
        if not textbook.is_borrowed:
            Textbook.update(is_borrowed=True).where(Textbook.book_id == book_id).execute()

    def return_book(self, book_id):
        """Set 'is_borrowed' attribute to false"""
        textbook = Textbook.select().where(Textbook.book_id == book_id).get()
        if textbook.is_borrowed:
            Textbook.update(is_borrowed=False).where(Textbook.book_id == book_id).execute()

    def to_dict(self) -> dict:
        """Return textbook instance state as a dictionary"""
        instance = dict(type=self.BOOK_TYPE, book_id=self.book_id, title=self.book_title, author=self.author,
                        published_year=self.published_year, edition=self.edition,
                        cover_type=self.cover_type, subject=self.book_subject,
                        is_borrowed=self.is_borrowed)
        return instance

    def __str__(self):
        """Special method to print Textbook """
        return f"<{self.book_id}, {self.book_title}, {self.author}, {self.published_year}," \
               f"{self.edition}, {self.cover_type}, {self.book_subject}, {self.is_borrowed}>"
