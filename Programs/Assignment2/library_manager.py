# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-02-20

"""The 'LibraryManager' class controls the library book records.
It can add or remove books from the records and manage the status of
books in terms of whether any book is borrowed or not and how many"""

from typing import List
from textbook import Textbook
from ebook import eBook
from library_stats import LibraryStats


class LibraryManager:
    """initiates the values needed to manage the book records"""
    def __init__(self, name):
        self._name = name
        self._book_record = {}

    @property
    def get_name(self) -> str:
        """returns the name of the librarian"""
        return self._name

    def add_book(self, book) -> None:
        """adds the books to book record"""
        if book not in self._book_record.values():
            self._book_record[book.get_book_id] = book
        else:
            raise LookupError('The book is already added to the library records.')

    def remove_book(self, book_id: str) -> None:
        """removes the added books to the library records"""
        if book_id in self._book_record:
            del self._book_record[book_id]
        else:
            raise KeyError(f'no books with the id {book_id} exists in the records')

    def get_book_by_id(self, book_id: str) -> (str, None):
        """returns the book object if its id exists in the library records"""
        if book_id in self._book_record:
            return self._book_record[book_id]
        else:
            return None

    def exists_in_library(self, book_id: str) -> bool:
        """returns true if the book exists in the library records"""
        if book_id in self._book_record:
            return True
        else:
            return False

    def get_all_books(self):
        """returns all the books in the library records"""
        if self._book_record:
            return self._book_record
        else:
            return []

    def get_book_stat(self):
        """counts the number of borrowed/not borrowed books.
        It also counts the number of textbooks and ebooks in
        the library records"""

        num_borrowed = 0
        num_not_borrowed = 0
        num_textbooks = 0
        num_ebooks = 0
        for book in self._book_record.values():
            if book.get_book_type == Textbook.BOOK_TYPE:
                num_textbooks += 1
            if book.get_book_type == eBook.BOOK_TYPE:
                num_ebooks += 1
            if book.get_availability_status():
                num_borrowed += 1
            else:
                num_not_borrowed += 1

        stat = LibraryStats(num_not_borrowed, num_borrowed, num_textbooks, num_ebooks)
        return stat

    def show_book_not_borrowed(self, type: str):
        """displays the description of the textbooks and ebooks available to borrow"""
        if type == "textbook" or type == "ebook":
            for book in self._book_record.values():
                if book.get_book_type == type:
                    if not book.get_availability_status():
                        book.display_info()
        else:
            raise ValueError("Invalid type. Please enter either of the types: 'textbook' or 'ebook'")

    def show_available_book_category(self, type: str) -> None:
        """displays all book (textbook/ebook) categories existing/
        available in the library in a table format"""
        max_length = self.max_book_len()
        self.draw_lable(type)
        if type == Textbook.BOOK_TYPE:
            Textbook.BOOK_SUBJECT.sort()
            for sub in Textbook.BOOK_SUBJECT:
                print('{:<12}'.format('|'), sub.ljust(max_length[0]), '{:>10}'.format('|'))
        else:
            eBook.BOOK_GENRE.sort()
            for gen in eBook.BOOK_GENRE:
                print('{:<8}'.format('|'), gen.ljust(max_length[1]), '{:>10}'.format('|'))

    def max_book_len(self) -> List:
        """returns the the max size element in ebook genre list and textbook subject list"""
        textbook_sub = max(len(sub) for sub in Textbook.BOOK_SUBJECT)
        ebook_gen = max(len(gen) for gen in eBook.BOOK_GENRE)
        return [textbook_sub, ebook_gen]

    def draw_lable(self, type: str) -> None:
        """draws the tables' top label"""
        max_length = self.max_book_len()
        if type == Textbook.BOOK_TYPE:
            print('+', end='')
            for i in range(max_length[0] * 3):
                print('-', end='')
            print('+')
        else:
            print('+', end='')
            for i in range(max_length[1] * 2):
                print('-', end='')
            print('+')






