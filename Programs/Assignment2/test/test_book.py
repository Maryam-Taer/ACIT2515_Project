# Maryam Taer
# Set 2C
# 2020-10-02

"""the test class 'TestVanProperty' uses python unittest to test the methods and constructor
in VanProperty to make sure that they are working right"""

from unittest import TestCase
from book import Book


class TestBook(TestCase):
    def setUp(self):
        """creates an object to be tested and to prevent redundancy in creating objects"""
        self.book = Book('B222', 'color methodology', 'Maryam Taer', 2002, 4, True)

    def test_constructor(self):
        """tests the constructor as a 'failure' test"""
        self.assertIsNotNone(self.book)
        self.assertIsInstance(self.book, Book)

        with self.assertRaises(TypeError):
            book = Book(22, 'color methodology', 'Maryam Taer', 2002, 4, True)

        with self.assertRaises(ValueError):
            book = Book('B2', 'color methodology', 'Maryam Taer', 2002, 4, True)

        with self.assertRaises(TypeError):
            book = Book('B222', 34, 'Maryam Taer', 2002, 4, True)

        with self.assertRaises(TypeError):
            book = Book('B222', 'color methodology', 1, 2002, 4, True)

        with self.assertRaises(TypeError):
            book = Book('B222', 'color methodology', 'Maryam Taer', '2002', 4, True)

        with self.assertRaises(ValueError):
            book = Book('B222', 'color methodology', 'Maryam Taer', 2021, 4, True)

        with self.assertRaises(TypeError):
            book = Book('B222', 'color methodology', 'Maryam Taer', 2002, '4', True)

        with self.assertRaises(ValueError):
            book = Book('B222', 'color methodology', 'Maryam Taer', 2002, 0, True)

    def test_get_book_id(self):
        """tests the address of the property"""
        self.assertEqual(self.book.get_book_id, 'B222')
        self.assertIsNotNone(self.book.get_book_id)

    def test_get_book_title(self):
        """tests the selling_status of the property"""
        self.assertEqual(self.book.get_book_title, 'color methodology')
        self.assertIsNotNone(self.book.get_book_title)

    def test_get_author(self):
        """tests and validates the number of the bedrooms of the 'prop' object instance"""
        self.assertEqual(self.book.get_author, 'Maryam Taer')
        self.assertIsNotNone(self.book.get_author)

    def test_get_published_year(self):
        """tests and validates the number of the bathrooms of the 'prop' object instance"""
        self.assertEqual(self.book.get_published_year(), 2002)
        self.assertIsNotNone(self.book.get_published_year())

    def test_get_edition(self):
        """tests and validates the neighborhood of the 'prop' object instance"""
        self.assertEqual(self.book.get_edition(), 4)
        self.assertIsNotNone(self.book.get_edition())

    def test_get_availability_status(self):
        """tests and validates the city of the 'prop' object instance"""
        self.assertEqual(self.book.get_availability_status(), True)
        self.assertIsNotNone(self.book.get_availability_status())

    def test_get_type(self):
        """tests and validates the abstract method of type the 'prop' object instance"""
        with self.assertRaises(NotImplementedError):
            self.book.get_book_type()

    def test_display_info(self):
        """tests and validates the abstract method of display_information the 'prop' object instance"""
        with self.assertRaises(NotImplementedError):
            self.book.display_info()








