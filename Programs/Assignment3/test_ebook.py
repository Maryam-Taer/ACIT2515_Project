# Maryam Taer
# Set 2C
# 2020-03-16

"""the test class 'TesteBook' uses python unittest to test the methods and constructor
in eBook to make sure that they are working right"""

from unittest import TestCase
from ebook import eBook


class TesteBook(TestCase):
    def setUp(self):
        """creates an object to be tested and to prevent redundancy in creating objects"""
        self.ebook = eBook('B20V2', 'Me', 'Elton John', 2017, 4, 'OverDrive Read', 'biography', False)

    def test_constructor(self):
        """tests the constructor as a 'failure' test"""
        self.assertIsNotNone(self.ebook)
        self.assertIsInstance(self.ebook, eBook)

        with self.assertRaises(TypeError):
            ebook = eBook('B20V2', 'Me', 'Elton John', 2017, 4, 2, 'biography', False)

        with self.assertRaises(ValueError):
            ebook = eBook('B20V2', 'Me', 'Elton John', 2017, 4, 'OverRead', 'biography', False)

        with self.assertRaises(TypeError):
            ebook = eBook('B20V2', 'Me', 'Elton John', 2017, 4, 'OverDrive Read', 34, False)

        with self.assertRaises(ValueError):
            ebook = eBook('B20V2', 'Me', 'Elton John', 2017, 4, 'OverDrive Read', 'bio', False)

    def test_get_book_type(self):
        """tests the book type of the house object"""
        self.assertEqual(self.ebook.get_book_type, 'ebook')
        self.assertIsNotNone(self.ebook.get_book_type)

    def test_get_book_platform(self):
        """tests the book platform"""
        self.assertEqual(self.ebook.get_book_platform, 'OverDrive Read')
        self.assertIsNotNone(self.ebook.get_book_platform)

    def test_set_book_platform(self):
        """tests the book platform"""
        self.ebook.set_book_platform('Fast Read Ebooks')
        self.assertEqual(self.ebook.get_book_platform, 'Fast Read Ebooks')
        self.assertIsNotNone(self.ebook.get_book_platform)
        with self.assertRaises(ValueError):
            self.ebook.set_book_platform('poem')

        with self.assertRaises(TypeError):
            self.ebook.set_book_platform(12)

    def test_get_available_platforms(self):
        """tests the available platforms in the library"""
        self.assertEqual(self.ebook.get_available_platforms, '\n '.join(self.ebook.PLATFORM))

    def test_get_book_genre(self):
        """tests the book genre"""
        self.assertEqual(self.ebook.get_book_genre, 'biography')
        self.assertIsNotNone(self.ebook.get_book_genre)

    def test_set_book_genre(self):
        """tests the book platform"""
        self.ebook.set_book_genre('comics')
        self.assertEqual(self.ebook.get_book_genre, 'comics')
        self.assertIsNotNone(self.ebook.get_book_genre)
        with self.assertRaises(ValueError):
            self.ebook.set_book_genre('poem')

        with self.assertRaises(TypeError):
            self.ebook.set_book_genre(23)

    def test_suffix(self):
        """tests the book edition suffix"""
        self.assertEqual(self.ebook.suffix(self.ebook.get_edition()), 'th')

    def test_to_dict(self):
        self.assertTrue(self.ebook.to_dict())
        self.assertEqual(self.ebook.to_dict(), {'id': 'B20V2', 'title': 'Me',
                                                'author': 'Elton John', 'published_year': 2017,
                                                'edition': 4, 'platform': 'OverDrive Read',
                                                'genre': 'biography', 'is_borrowed': False})

    def test_display_info(self):
        """tests the description of the ebook object to make sure it returns none but prints the description"""
        self.assertFalse(self.ebook.get_availability_status())
        self.assertEqual(self.ebook.display_info(), None)

        self.ebook1 = eBook('L091A', 'Deadpool Vol.4: Monkey Business', 'Daniel Way', 2019, 5,
                            'Fast Read Ebooks', 'comics', True)
        self.assertTrue(self.ebook1.get_availability_status())
        self.assertEqual(self.ebook1.display_info(), None)
