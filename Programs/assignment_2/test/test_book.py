import unittest

from book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book1 = Book('B222', 'color methology', 'Maryam Taer', 2002, 4, True)


    def test_constructor(self):
        """ valid constructor"""
        self.assertIsInstance(self.book1, Book)

    def test_get_book_id(self):
        """ Test if function returns correct ID """
        self.assertIs(self.book1.get_book_id, 'B222')

    def test_get_book_title(self):
        """ Test if function returns correct Title """
        self.assertEqual(self.book1.get_book_title, 'color methology')

    def test_get_author(self):
        """ Test if function returns correct author """
        self.assertEqual(self.book1.get_author, 'Maryam Taer')

    def test_get_published_year(self):
        """ Test if function returns correct published year """
        self.assertEqual(self.book1.get_published_year(), 2002)

    def test_get_edition(self):
        """ Test if function returns correct edition """
        self.assertEqual(self.book1.get_edition(), 4)

    def test_get_availability_status(self):
        """ Test iffunction returns correct availability status """
        self.assertIs(self.book1.get_availability_status(), True)

    def test_get_book_type(self):
        """ test to see if function raise NotImplementationError """
        with self.assertRaises(NotImplementedError):
            self.book1.get_book_type()

    def test_display_info(self):
        """ test to see if function raise NotImplementationError """
        with self.assertRaises(NotImplementedError):
            self.book1.display_info()

    def test_validation_fail(self):
        """ test to see if constructor raises an error when given wrong parameters """

        with self.assertRaises(TypeError):
            self.book_fail = Book(12, 10, 'Maryam Taer', 2002, 4, True)

        with self.assertRaises(TypeError):
            self.book_fail = Book('asd', 10, 'Maryam Taer', 2002, 4, True)

        with self.assertRaises(TypeError):
            self.book_fail = Book('asd', '10', 13, 2002, 4, True)

        with self.assertRaises(TypeError):
            self.book_fail = Book('asd', '10', 'Maryam Taer', '2002', 4, True)

        with self.assertRaises(TypeError):
            self.book_fail = Book('asd', '10', 'Maryam Taer', 20020, 4, True)

        with self.assertRaises(TypeError):
            self.book_fail = Book('asd', '10', 'Maryam Taer', 2002, '4', True)

        with self.assertRaises(TypeError):
            self.book_fail = Book('asd', '10', 'Maryam Taer', 2002, -3, True)






    #
    # def test_constructor(self):
    #     """ valid construction """
    #     self.assertIsInstance(self.book1, Book)
    #
    # def test_get_availability_status(self):
    #     """ test if function returns right boolean status """
    #     self.assertIs(self.book1.get_availabilty_status(), False)
    #
    # def test_get_id(self):
    #     """ test if function returns right id """
    #     self.assertIs(self.book1.get_id(), 'book_id')
    #
    # def test_get_book_title(self):
    #     """ test if function returns right title """
    #     self.assertIs((self.book1.get_book_title()), 'book_title')
    #
    # def test_get_author(self):
    #     """ test if function returns right author """
    #     self.assertIs(self.book1.get_author(), 'author')
    #
    # def test_get_published_year(self):
    #     """ test if function returns right published year """
    #     self.assertEqual(self.book1.published_year(), 2000)
    #
    # def test_get_edition(self):
    #     """ test if function returns right edition"""
    #     self.assertEqual(self.book1.get_edition(), 111)
    #
    # def test_get_type(self):
    #     """ test to see if function raise NotImplementationError """
    #     with self.assertRaises(NotImplementedError):
    #         self.book1.get_type()
    #
    # def test_display_info(self):
    #     """ test to see if function raise NotImplementationError """
    #     with self.assertRaises(NotImplementedError):
    #         self.book1.display_info()
