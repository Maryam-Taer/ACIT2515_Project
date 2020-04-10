# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-03-16


from unittest import TestCase
from peewee import SqliteDatabase
from models.ebook import eBook
from models.textbook import Textbook
from models.library_stats import LibraryStats
from models.library_manager import LibraryManager

test_db = SqliteDatabase("TestBook.db")
test_db.connect()


class TestLibraryManager(TestCase):
    def setUp(self):
        """ Create tables in db & Create test data """
        test_db.create_tables([eBook, Textbook])
        self.library1 = LibraryManager(name='The_library')
        self.book1 = eBook(book_id='B20V2', book_title='Me', author='Elton John', published_year=2017,
                           edition=4, platform='OverDrive Read', book_genre='biography', is_borrowed=True)
        self.book3 = Textbook(book_id='A110', book_title='why do we sleep?', author='John Simpliciano',
                              published_year=2015, edition=3, cover_type='hardcover case wrap',
                              book_subject='health', is_borrowed=True)

    def tearDown(self):
        """ Drop tables in db """
        test_db.drop_tables([eBook, Textbook])

    def test_constructor(self):
        """ Valid constructor """
        self.assertIsInstance(self.library1, LibraryManager)

    def test_add_book(self):
        """ Test if function adds to the library """
        self.tearDown()
        self.setUp()
        self.library1.add_book(self.book1)

    def test_add_book_fail(self):
        """ Test if function raises error when add book to library """
        self.library1.clear_record()
        self.tearDown()
        self.setUp()
        self.library1.add_book(self.book1)
        with self.assertRaises(ValueError):
            self.library1.add_book(self.book1)

    def test_remove_book(self):
        """ Test if function removes from inventory """
        self.book2 = Textbook(book_id='A111', book_title='why do we need to sleep?', author='John Simpliciano',
                              published_year=2017, edition=9, cover_type='hardcover case wrap', book_subject='health')
        self.library1.clear_record()
        self.tearDown()
        self.setUp()
        self.library1.add_book(self.book2)
        self.library1.add_book(self.book1)
        self.library1.remove_book('A111')
        self.library1.remove_book('B20V2')

    def test_remove_book_fail(self):
        """ test if function raises error when book with no id exists """
        with self.assertRaises(KeyError):
            self.library1.remove_book('B20DS')

    def test_update_book(self):
        """ Test the success samples of update book performance """
        self.library1.clear_record()
        self.tearDown()
        self.setUp()
        self.library1.add_book(self.book1)
        self.library1.add_book(self.book3)
        self.library1.update_book('B20V2', 'Fast Read Ebooks', 'mystery')
        self.library1.update_book('A110', 'chemistry', 'paperback')

    def test_update_book_fail(self):
        """ Test the failure sample of update book performance """
        self.library1.clear_record()
        self.tearDown()
        self.setUp()
        self.library1.add_book(self.book1)
        self.library1.add_book(self.book3)
        with self.assertRaises(ValueError):
            self.library1.update_book('B20V2', 'Something', 'language')

        with self.assertRaises(ValueError):
            self.library1.update_book('A110', 'Something', 'language')

        self.assertIsNone(self.library1.update_book('B203', 'Something', 'language'))

    def test_to_dict(self):
        """ Test the performance of converting objects to json dictionary """
        self.library1.clear_record()
        self.tearDown()
        self.setUp()
        self.library1.add_book(self.book1)
        self.assertTrue(self.library1.to_dict())

    def test_get_book_by_id(self):
        """ Test if function returns correct book by id"""
        self.library1.clear_record()
        self.tearDown()
        self.setUp()
        self.library1.add_book(self.book1)
        self.assertIsNotNone(self.library1.get_book_by_id('B20V2'))

    def test_get_book_stats(self):
        """ Test if function returns inventory stats """
        self.library1.clear_record()
        self.tearDown()
        self.setUp()
        self.library1.add_book(self.book1)
        self.library1.add_book(self.book3)
        self.assertIsInstance(self.library1.get_book_stat(), LibraryStats)

    def test_get_book_by_type(self):
        """ Test if function returns all Books by type """
        self.library1.clear_record()
        self.tearDown()
        self.setUp()
        self.library1.add_book(self.book1)
        self.library1.add_book(self.book3)
        self.library1.get_books_by_type('ebook')
        self.library1.get_books_by_type('textbook')
        self.library1.get_books_by_type('someOtherType')