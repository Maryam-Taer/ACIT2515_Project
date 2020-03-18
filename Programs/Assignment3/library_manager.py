# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-03-16

"""The 'LibraryManager' class controls the library book records.
It can add or remove books from the records and manage the status of
books in terms of whether any book is borrowed or not and how many"""

import json
from typing import List
from textbook import Textbook
from ebook import eBook
from library_stats import LibraryStats


class LibraryManager:
    """initiates the values needed to manage the book records"""

    def __init__(self, name):
        self._name = name
        self._book_record = {}
        self._filepath = 'library_manager.json'
        self.write_to_file()
        self._read_from_file(self._filepath)

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
        self.write_to_file()

    def write_to_file(self):
        """writes the instance to the library_manager.json file """
        book = self.to_dict()
        book['ebook'] = list({b['id']: b for b in book['ebook']}.values())
        book['textbook'] = list({b['id']: b for b in book['textbook']}.values())
        record_json = json.dumps(book, indent=4)

        with open(self._filepath, 'w') as file:
            file.write(record_json)
        return record_json

    def _read_from_file(self, path):
        """reads the instance from the library_manager.json file
           creates entities accordingly"""
        try:
            with open(path, 'r') as file:
                entity = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f'{path} does not exist.')

        for ebook in entity["ebook"]:
            self.from_dict(ebook, 'ebook')
        for textbook in entity["textbook"]:
            self.from_dict(textbook, 'textbook')

    def remove_book(self, book_id: str) -> None:
        """removes the added books to the library records"""
        if book_id in self._book_record:
            del self._book_record[book_id]
        else:
            raise KeyError(f'no books with the id {book_id} exists in the records')

    def update_book(self, book_id: str, arg1: str, arg2: str):
        """ updates some instances of textbook & ebook
            raises Exception if the books do not exist (or values are not correct) """
        book = self.get_book_by_id(book_id)

        if not book:
            raise ValueError("Book is not in the records.")
        if book.get_book_type == "textbook":
            book.set_book_subject(arg1)
            book.set_cover_type(arg2)
        elif book.get_book_type == "ebook":
            book.set_book_platform(arg1)
            book.set_book_genre(arg2)

        self.write_to_file()

    def to_dict(self):
        """ Return textbook instance state as a JSON dictionary """
        output = dict()
        output["name"] = self._name
        output["ebook"] = list()
        output["textbook"] = list()
        for book in self._book_record.values():
            if book.get_book_type == "textbook":
                output["textbook"].append(book.to_dict())
            elif book.get_book_type == "ebook":
                output["ebook"].append(book.to_dict())
        return output

    @staticmethod
    def from_dict(book_dict: dict, book_type: str):
        """ Return textbook instance state from JSON format as dictionary """
        global instance
        if book_type == "ebook":
            instance = eBook(book_dict["id"], book_dict["title"], book_dict["author"],
                             book_dict["published_year"], book_dict["edition"],
                             book_dict["platform"], book_dict["genre"], book_dict["is_borrowed"])

        elif book_type == "textbook":
            instance = Textbook(book_dict["id"], book_dict["title"], book_dict["author"],
                                book_dict["published_year"], book_dict["edition"],
                                book_dict["cover_type"], book_dict["subject"], book_dict["is_borrowed"])
        return instance

    def get_book_by_id(self, book_id: str) -> (object, None):
        """returns the book object if its id exists in the library records"""
        if book_id in self._book_record:
            return self._book_record[book_id]
        else:
            return None

    def get_books_by_type(self, book_type: str):
        """returns the all book object based on their type"""
        return [book.to_dict() for book in self._book_record.values() if book.get_book_type == book_type]

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

    def show_book_not_borrowed(self, book_type: str):
        """displays the description of the textbooks and ebooks available to borrow"""
        if book_type == "textbook" or book_type == "ebook":
            for book in self._book_record.values():
                if book.get_book_type == book_type:
                    if not book.get_availability_status():
                        book.display_info()
        else:
            raise ValueError("Invalid type. Please enter either of the types: 'textbook' or 'ebook'")

    def show_available_book_category(self, book_type: str) -> None:
        """displays all book (textbook/ebook) categories existing/
        available in the library in a table format"""
        max_length = self.max_book_len()
        self.draw_label(book_type)
        if book_type == Textbook.BOOK_TYPE:
            Textbook.BOOK_SUBJECT.sort()
            for sub in Textbook.BOOK_SUBJECT:
                print('{:<12}'.format('|'), sub.ljust(max_length[0]), '{:>10}'.format('|'))
        else:
            eBook.BOOK_GENRE.sort()
            for gen in eBook.BOOK_GENRE:
                print('{:<8}'.format('|'), gen.ljust(max_length[1]), '{:>10}'.format('|'))

    @staticmethod
    def max_book_len() -> List:
        """returns the the max size element in ebook genre list and textbook subject list"""
        textbook_sub = max(len(sub) for sub in Textbook.BOOK_SUBJECT)
        ebook_gen = max(len(gen) for gen in eBook.BOOK_GENRE)
        return [textbook_sub, ebook_gen]

    def draw_label(self, book_type: str) -> None:
        """draws the tables' top label"""
        max_length = self.max_book_len()
        if book_type == Textbook.BOOK_TYPE:
            print('+', end='')
            for i in range(max_length[0] * 3):
                print('-', end='')
            print('+')
        else:
            print('+', end='')
            for i in range(max_length[1] * 2):
                print('-', end='')
            print('+')
