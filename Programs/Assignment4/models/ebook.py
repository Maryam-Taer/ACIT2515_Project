# Group 16
# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-04-08

"""This is the child class of 'Book' class that inherits common attributes
initiated in the 'Book' class while specifying its own attributes that
distinguishes a 'eBook' with other type of books"""

from .book import Book
from peewee import CharField, UUIDField


class eBook(Book):
    BOOK_TYPE = 'ebook'
    PLATFORM = ['OverDrive Read', 'Fast Read ebooks']
    BOOK_GENRE = ['biography', 'kids', 'business & finance', 'romance',
                  'mystery', 'comics', 'fantasy', 'notification', 'literature', 'periodicals']

    """initiates all the special attributes of a book as well as inheriting the common attributes"""
    platform = CharField()
    book_genre = CharField(column_name='genre')

    def borrow(self, book_id: str) -> None:
        """ Set 'is_borrowed' attribute to true """
        ebook = eBook.select().where(eBook.book_id == book_id).get()
        if not ebook.is_borrowed:
            eBook.update(is_borrowed=True).where(eBook.book_id == book_id).execute()

    def return_book(self, book_id: str) -> None:
        """ Set 'is_borrowed' attribute to false """
        ebook = eBook.select().where(eBook.book_id == book_id).get()
        if ebook.is_borrowed:
            eBook.update(is_borrowed=False).where(eBook.book_id == book_id).execute()

    def get_book_type(self) -> str:
        """ Return book type """
        return self.BOOK_TYPE

    def to_dict(self) -> dict:
        """ Return ebook instance state as a dictionary """
        instance = dict(type=self.BOOK_TYPE, book_id=self.book_id, title=self.book_title, author=self.author,
                        published_year=self.published_year, edition=self.edition,
                        platform=self.platform, genre=self.book_genre,
                        is_borrowed=self.is_borrowed)
        return instance

    def __str__(self):
        """ Special method to print eBook instances"""
        return f"<{self.book_id}, {self.book_title}, {self.author}, {self.published_year}," \
               f"{self.edition}, {self.platform}, {self.book_genre}, {self.is_borrowed}>"