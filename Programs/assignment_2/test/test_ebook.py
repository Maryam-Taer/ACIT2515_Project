import unittest

from ebook import eBook

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book1 = eBook('B20V2', 'Me', 'Elton John', 2017, 4, 'OverDrive Read', 'biography', False)

    def test_constructor(self):
        """ valid constructor"""
        self.assertIsInstance(self.book1, eBook)

    def test_get_book_type(self):
        """ Test if function returns correct type """
        self.assertIs(self.book1.get_book_type, 'ebook')

    def test_get_book_platform(self):
        """ Test if function returns correct platform """
        self.assertEqual(self.book1.get_book_platform, 'OverDrive Read')

    def test_get_available_platforms(self):
        """ Test if function returns correct available platforms """
        self.assertEqual(self.book1.get_available_platforms, ['OverDrive Read', 'Fast Read Ebooks'])

    def test_get_book_genre(self):
        """ Test if function returns correct genre """
        self.assertEqual(self.book1.get_book_genre, 'biography')

    def test_suffix(self):
        self.assertEqual(self.book1.suffix(4), 'th')


    def test_display_info(self):
        """ test function if it prints correct output when status is False"""
        self.assertIsNone(self.book1.display_info())


    def test_display_info_true(self):
        """ test function if it prints correct output when status is True"""
        self.book1 = eBook('B20V2', 'Me', 'Elton John', 2017, 4, 'OverDrive Read', 'biography', True)
        self.assertIsNone(self.book1.display_info())


    # def test_validate(self):
    #     """ test to see if constructor raises an error when given wrong parameters """
    #     with self.assertRaises(ValueError):
    #         self.fail_book = eBook('B20V2', 'Me', 'Elton John', 2017, 4, '12', 'biography', False)
