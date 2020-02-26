# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-02-20

"""The program creates a 'Book' object in 'Book' class to display the
book information needed for a customer who needs to borrow a book.
It also provides information on the book availability status; meaning
whether a book has been borrowed already or not"""


class Book:
    """initiates all the common attributes of a book"""
    MIN_EDITION = 1
    MIN_PUBLISHED_YEAR = 1920
    MAX_PUBLISHED_YEAR = 2020

    def __init__(self, book_id, book_title, author, published_year, edition, is_borrowed):
        self._book_id = book_id
        self._book_title = book_title
        self._author = author
        self._published_year = published_year
        self._edition = edition
        self._is_borrowed = is_borrowed
        self.validation(book_id, book_title, author, published_year, edition)

    @property
    def get_book_id(self) -> str:
        """returns the book_id"""
        return self._book_id

    @property
    def get_book_title(self) -> str:
        """returns the title of the book"""
        return self._book_title

    @property
    def get_author(self) -> str:
        """returns the author of the book"""
        return self._author

    def get_published_year(self) -> int:
        """returns the year when the book was published"""
        return self._published_year

    def get_edition(self) -> int:
        """returns the edition of the book"""
        return self._edition

    def get_availability_status(self) -> bool:
        """returns the availability status of the book (borrowed: True/False)"""
        return self._is_borrowed

    def get_book_type(self) -> None:
        """abstract method of the book type -> to be used in child classes"""
        raise NotImplementedError()

    def display_info(self) -> None:
        """abstract method of the book information -> to be used in child classes"""
        raise NotImplementedError()

    @classmethod
    def validation(cls, book_id: str, book_title: str, author: str, published_year: int, edition: int) -> None:
        if type(book_id) != str:
            raise TypeError('Invalid book id! PLease enter the right id (e.g. s0124)')
        if type(book_title) != str:
            raise TypeError(f'Book with the title {book_title} not found.')
        if type(author) != str:
            raise TypeError(f'No book written by {author} found.')
        if type(published_year) != int:
            raise TypeError('Invalid published year! PLease enter again')
        if published_year < cls.MIN_PUBLISHED_YEAR or published_year > cls.MAX_PUBLISHED_YEAR:
            raise TypeError('Books published between 1995 and 2020 available in the library only.')
        if type(edition) != int:
            raise TypeError('invalid edition type! PLease enter again')
        if edition < cls.MIN_EDITION:
            raise TypeError(f'The edition {edition} of this book does not exist in the library.')