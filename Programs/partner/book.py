# from textbook import Textbook

class Book:
    def __init__(self, book_id, book_title, author, published_year, edition, is_borrowed):
        self._book_id = book_id
        self._book_title = book_title
        self._author = author
        self._published_year = published_year
        self._edition = edition
        self._is_borrowed = is_borrowed

    def is_borrowed(self):
        return self._is_borrowed

    def get_id(self):
        return self._book_id

    def get_book_title(self):
        return self._book_title

    def get_author(self):
        return self._author

    def published_year(self):
        return self._published_year

    def get_edition(self):
        raise NotImplementedError()

    def get_type(self):
        raise NotImplementedError()

    def display_info(self):
        raise NotImplementedError()




