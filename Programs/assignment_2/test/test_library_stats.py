import unittest

from library_stats import LibraryStats

class TestBook(unittest.TestCase):

    def setUp(self):
        self.stats = LibraryStats(1, 2, 3, 4)

    def test_constructor(self):
        """ Valid Constructor """
        self.assertIsInstance(self.stats, LibraryStats)

    def test_get_num_not_borrowed(self):
        """ test if function returns correct number of books not borrowed"""
        self.assertEqual(self.stats.get_num_not_borrowed(), 1)

    def test_get_num_borrowed(self):
        """ test if function returns correct number of books borrowed"""
        self.assertEqual(self.stats.get_num_borrowed(), 2)

    def test_get_num_textbooks(self):
        """ test if function returns correct number of books borrowed"""
        self.assertEqual(self.stats.get_num_textbooks(), 3)

    def test_get_num_ebooks(self):
        """ test if function returns correct number of books borrowed"""
        self.assertEqual(self.stats.get_num_ebooks(), 4)

    def test_validate(self):
        """ test if function raises error when parameters are wrong"""
        with self.assertRaises(ValueError):
            self.stats = LibraryStats(-1, -1, -1, 4)

        with self.assertRaises(ValueError):
            self.stats = LibraryStats('-1', '-1', '-1', '4')