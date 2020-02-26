import unittest

from textbook import Textbook

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book1 = Textbook('A111', 'why do we need to sleep?', 'John Simpliciano', 2017, 9, 'hardcover case wrap',
                         'health', False)

    def test_constructor(self):
        """ valid constructor """
        self.assertIsInstance(self.book1, Textbook)

    def test_get_book_type(self):
        """ Test if function returns correct type """
        self.assertIs(self.book1.get_book_type, 'textbook')

    def test_get_book_subject(self):
        """ Test if function returns correct subject """
        self.assertEqual(self.book1.get_book_subject, 'health')

    def test_get_cover_type(self):
        """ Test if function returns correct cover type """
        self.assertEqual(self.book1.get_cover_type, 'hardcover case wrap')

    def test_get_available_cover_types(self):
        """ Test if function returns correct available cover type """
        self.assertEqual(self.book1.get_available_cover_types, ['paperback', 'hardcover case wrap', 'hardcover dust jacket'])

    def test_suffix(self):
        """ test if function returns correct suffix """
        self.assertEqual(self.book1.suffix(4), 'th')

    def test_display_info(self):
        """ test function if it prints correct output when status is False"""
        self.assertIsNone(self.book1.display_info())


    def test_display_info_true(self):
        """ test function if it prints correct output when status is True"""
        self.book1 = Textbook('A111', 'why do we need to sleep?', 'John Simpliciano', 2017, 9, 'hardcover case wrap',
                         'health', True)
        self.assertIsNone(self.book1.display_info())

    def test_validate(self):
        """ Test if function raises an error when given wrong parameters """
        with self.assertRaises(TypeError):
            self.book1 = Textbook('A111', 'why do we need to sleep?', 'John Simpliciano', 2017, 9,
                                  12, 'health', False)
        with self.assertRaises(ValueError):
            self.book1 = Textbook('A111', 'why do we need to sleep?', 'John Simpliciano', 2017, 9,
                                  '12', 'health', False)

        with self.assertRaises(TypeError):
            self.book1 = Textbook('A111', 'why do we need to sleep?', 'John Simpliciano', 2017, 9,
                                  'hardcover case wrap', 12, False)

        with self.assertRaises(ValueError):
            self.book1 = Textbook('A111', 'why do we need to sleep?', 'John Simpliciano', 2017, 9,
                                  'hardcover case wrap', '12', False)

