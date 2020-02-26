# Maryam Taer
# Set 2C
# 2020-10-02

"""the test class 'TestHouse' uses python unittest to test the methods and constructor
in VanProperty to make sure that they are working right"""

from unittest import TestCase
from textbook import Textbook


class TestTextbook(TestCase):
    def setUp(self):
        """creates an object to be tested and to prevent redundancy in creating objects"""
        self.textbook = Textbook('V654', 'Hamlet', 'Shakespeare', 2000, 3, 'hardcover dust jacket', 'literature', True)

    def test_constructor(self):
        """tests the constructor as a 'success' and 'failure' test"""
        self.assertIsNotNone(self.textbook)
        self.assertIsInstance(self.textbook, Textbook)

        with self.assertRaises(TypeError):
            textbook = Textbook('V654', 'Hamlet', 'Shakespeare', 2000, 10, 2, 'literature', True)

        with self.assertRaises(ValueError):
            textbook = Textbook('V654', 'Hamlet', 'Shakespeare', 2000, 10, 'hardcover dust', 'literature', True)

        with self.assertRaises(TypeError):
            textbook = Textbook('V654', 'Hamlet', 'Shakespeare', 2000, 3, 'hardcover dust jacket', 3, True)

        with self.assertRaises(ValueError):
            textbook = Textbook('V654', 'Hamlet', 'Shakespeare', 2000, 10, 'hardcover dust jacket', 'kids', True)

    def test_get_book_type(self):
        """tests the number of storeys of the house object"""
        self.assertEqual(self.textbook.get_book_type, 'textbook')
        self.assertIsNotNone(self.textbook.get_book_type)

    def test_get_book_subject(self):
        """tests the type of the house object (in this case -> 'house')"""
        self.assertEqual(self.textbook.get_book_subject, 'literature')
        self.assertIsNotNone(self.textbook.get_book_subject)

    def test_get_cover_type(self):
        """tests the type of the house object (in this case -> 'house')"""
        self.assertEqual(self.textbook.get_cover_type, 'hardcover dust jacket')
        self.assertIsNotNone(self.textbook.get_cover_type)

    def test_get_available_cover_types(self):
        """tests the type of the house object (in this case -> 'house')"""
        self.assertEqual(self.textbook.get_available_cover_types, '\n '.join(self.textbook.COVER_TYPE))
        self.assertIsNotNone(self.textbook.get_available_cover_types)

    def test_suffix(self):
        """tests the floor suffix of the condo object to make sure it returns the right suffix"""
        self.assertEqual(self.textbook.suffix(self.textbook.get_edition()), 'rd')

    def test_display_info(self):
        """tests the description of the house object to make sure it returns none but prints the description"""
        self.assertTrue(self.textbook.get_availability_status())
        self.assertEqual(self.textbook.display_info(), None)

        self.textbook = Textbook('A111', 'why do we need to sleep?', 'John Simpliciano', 2017, 9,
                                 'hardcover case wrap', 'health', False)
        self.assertFalse(self.textbook.get_availability_status())
        self.assertEqual(self.textbook.display_info(), None)

