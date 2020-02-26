import unittest

from library_manager import LibraryManager
from library_stats import LibraryStats
from textbook import Textbook
from ebook import eBook

class TestLibraryManager(unittest.TestCase):
    def setUp(self):
        self.library1 = LibraryManager('The_library')
        self.book1 = eBook('B20V2', 'Me', 'Elton John', 2017, 4, 'OverDrive Read', 'biography', False)
        self.book2 = Textbook('A111', 'why do we need to sleep?', 'John Simpliciano', 2017, 9, 'hardcover case wrap',
                         'health', False)

    def test_constructor(self):
        """ valid constructor """
        self.assertIsInstance(self.library1, LibraryManager)

    def test_get_name(self):
        """ test if function returns correct name"""
        self.assertEqual(self.library1.get_name, 'The_library')

    def test_add_book(self):
        """ test if function adds to the inventory """
        self.library1.add_book(self.book1)

    def test_add_book_fail(self):
        """ test if function raises error when book in library """
        with self.assertRaises(LookupError):
            self.library1.add_book(self.book1)
            self.library1.add_book(self.book1)

    def test_remove_book(self):
        """ test if function removes from inventory """
        self.library1.add_book(self.book1)
        self.library1.remove_book('B20V2')

    def test_remove_book_fail(self):
        """ test if function raises error when book with no id exists """
        with self.assertRaises(KeyError):
            self.library1.remove_book('B20V2')

    def test_get_book_by_id(self):
        """ test if function returns correct book by id"""
        self.library1.add_book(self.book1)
        self.assertIsNone(self.library1.get_book_by_id('B202'))


    def test_exist_in_library(self):
        """ Test if book exist in library by id """
        self.library1.add_book(self.book1)
        self.assertIs(self.library1.exists_in_library('B20V2'), True)
        self.assertIs(self.library1.exists_in_library('B2V2'), False)


    def test_get_all_books(self):
        """ test if function returns all books in inventory """
        self.assertEqual(self.library1.get_all_books(), [])
        self.library1.add_book(self.book1)
        self.assertEqual(type(self.library1.get_all_books()), dict)

    def test_get_book_stats(self):
        """ test if function returns inventory stats """
        self.library1.add_book(self.book1)
        self.library1.add_book(self.book2)
        self.assertIsInstance(self.library1.get_book_stat(), LibraryStats)

    def test_show_book_not_borrowed(self):
        """ Test if function displays description"""
        self.library1.add_book(self.book1)
        self.library1.add_book(self.book2)
        self.library1.show_book_not_borrowed("textbook")

    def test_show_book_not_borrowed_fail(self):
        """ Test if function raises an error """
        with self.assertRaises(ValueError):
            self.library1.show_book_not_borrowed("asd")
            
    def test_show_available_book_category(self):
        """ test if function display correct book categories"""
        self.library1.add_book(self.book1)
        self.library1.add_book(self.book2)
        self.library1.show_available_book_category('textbook')
        self.library1.show_available_book_category('ebook')