# Group 16
# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-04-08

"""The 'LibraryManager' class controls the library book records.
It can add or remove books from the records and manage the status of
books in terms of whether any book is borrowed or not and how many"""

from database.database import db
from .ebook import eBook
from .textbook import Textbook
from .library_stats import LibraryStats
from peewee import Model, CharField


class LibraryManager(Model):
    """initiates the values needed to manage the book records"""
    name = CharField(unique=True)
    book_id_record = {}

    class Meta:
        database = db

    def clear_record(self) -> None:
        """ Clear 'book_id_record' dictionary """
        self.book_id_record.clear()

    def add_book(self, book) -> None:
        """ Add the books to db """
        if book.book_id in self.book_id_record:
            raise ValueError('Invalid ID! Please enter a unique ID.')
        else:
            self.book_id_record[book.book_id] = book.BOOK_TYPE
            book.save()

    def remove_book(self, book_id: str) -> None:
        """ Remove the added books from db """
        if book_id not in self.book_id_record:
            raise KeyError(f'Book with ID {book_id} does not exist.')
        else:
            if self.book_id_record[book_id] == 'ebook':
                eBook.get(eBook.book_id == book_id).delete_instance()
            elif self.book_id_record[book_id] == 'textbook':
                Textbook.get(Textbook.book_id == book_id).delete_instance()
            del self.book_id_record[book_id]

    def update_book(self, book_id: str, arg1: str, arg2: str):
        """ updates some instances of textbook & ebook
            raises Exception if the books do not exist (or values are not correct) """
        book = self.get_book_by_id(book_id)

        if not book:
            return None

        if book.get_book_type() == "textbook":
            if arg1 not in book.BOOK_SUBJECT or arg2 not in book.COVER_TYPE:
                raise ValueError('Invalid entry!')
            else:
                Textbook.update(book_subject=arg1, cover_type=arg2).where(Textbook.book_id == book_id).execute()
        elif book.get_book_type() == "ebook":
            if arg1 not in book.PLATFORM or arg2 not in book.BOOK_GENRE:
                raise ValueError('Invalid entry!')
            else:
                eBook.update(platform=arg1, book_genre=arg2).where(eBook.book_id == book_id).execute()

    def get_book_by_id(self, book_id: str) -> (object, None):
        """ Return the book object if its id exists in the 'Book' db """
        if book_id not in self.book_id_record:
            return None
        else:
            if self.book_id_record[book_id] == 'ebook':
                return eBook.select().where(eBook.book_id == book_id).get()
            else:
                return Textbook.select().where(Textbook.book_id == book_id).get()

    @staticmethod
    def get_books_by_type(book_type: str) -> (list, None):
        """ Return the all book object based on their type """
        if book_type == eBook.BOOK_TYPE:
            return [book.to_dict() for book in eBook.select()]
        elif book_type == Textbook.BOOK_TYPE:
            return [book.to_dict() for book in Textbook.select()]
        else:
            return None

    def to_dict(self) -> dict:
        """ Return Textbook & eBook instance state as a JSON dictionary """
        output = dict()
        output["name"] = self.name
        output["ebook"] = list(book.to_dict() for book in eBook.select())
        output["textbook"] = list(book.to_dict() for book in Textbook.select())
        return output

    @staticmethod
    def get_book_stat():
        """ Calculate the statistics of eBook and Textbook instances """
        num_ebooks = 0
        num_textbooks = 0
        num_books = 0
        borrowed_ebooks = 0
        borrowed_textbooks = 0
        for ebook in eBook.select():
            if ebook.is_borrowed:
                borrowed_ebooks += 1
            num_ebooks += 1
            num_books += 1
        for textbook in Textbook.select():
            if textbook.is_borrowed:
                borrowed_textbooks += 1
            num_textbooks += 1
            num_books += 1
        borrowed_books = borrowed_ebooks + borrowed_textbooks

        stat = LibraryStats(num_ebooks, num_textbooks, num_books, borrowed_ebooks, borrowed_textbooks, borrowed_books)
        return stat
