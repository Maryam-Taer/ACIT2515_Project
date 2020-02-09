

from book import Book

class eBook(Book):
    def __init__(self, book_id, book_title, author, published_year, edition, is_borrowed, platform, book_category):
        super().__init__(book_id, book_title, author, published_year, edition, is_borrowed)
        self._platform = platform
        self._book_category = book_category


    def display_info(self):
        return self._book_id, self._book_title, self._author, self._published_year, self._edition, self._is_borrowed,\
               self._platform, self._book_category


    def get_edition(self):
        return self._book_id


    def get_type(self):
        return self._platform
