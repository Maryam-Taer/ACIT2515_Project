

from book import Book


class Textbook(Book):
    def __init__(self, book_id, book_title, author, published_year, edition, is_borrowed, cover_type, book_subject):
        super().__init__(book_id, book_title, author, published_year, edition, is_borrowed)
        self._cover_type = cover_type
        self._book_subject = book_subject



    def display_info(self):
        return self._book_id, self._book_title, self._author, self._published_year, self._edition, self._is_borrowed,\
               self._cover_type, self._book_subject


    def get_edition(self):
        return self._book_id


    def get_type(self):
        return self._cover_type




