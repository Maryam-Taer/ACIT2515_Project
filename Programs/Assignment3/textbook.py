# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-03-16

"""This is the child class of 'Book' class that inherits common attributes
initiated in the 'Book' class while specifying its own attributes that
distinguishes a 'text book' with other type of books"""

from book import Book


class Textbook(Book):
    BOOK_TYPE = 'textbook'
    COVER_TYPE = ['paperback', 'hardcover case wrap', 'hardcover dust jacket']
    BOOK_SUBJECT = ['language', 'biology', 'health', 'english', 'french', 'arts',
                    'music', 'science', 'psychology', 'math', 'poetry', 'history',
                    'chemistry', 'physics', 'literature', 'short story']

    """initiates all the special attributes of a book as well as inheriting the common attributes"""

    def __init__(self, book_id, book_title, author, published_year, edition, cover_type, book_subject, is_borrowed):
        super().__init__(book_id, book_title, author, published_year, edition, is_borrowed)
        self._cover_type = cover_type
        self._book_subject = book_subject
        self.validate(cover_type, book_subject)

    @property
    def get_book_type(self) -> str:
        """returns the type of the book"""
        return self.BOOK_TYPE

    @property
    def get_book_subject(self) -> str:
        """returns the textbook subject in the library"""
        return self._book_subject

    def set_book_subject(self, subject: str) -> None:  # FIX_ME
        """sets the textbook subjects in the library"""
        if type(subject) is not str:
            raise TypeError("Invalid cover type")
        if subject not in self.BOOK_SUBJECT:
            raise ValueError("Invalid cover type")
        self._book_subject = subject

    @property
    def get_cover_type(self) -> str:
        """returns the textbook cover_type in the library"""
        return self._cover_type

    def set_cover_type(self, cover_type) -> None:  # FIX_ME
        """sets the textbook cover type in the library"""
        if type(cover_type) is not str:
            raise TypeError("Invalid cover type")
        if cover_type not in self.COVER_TYPE:
            raise ValueError("Invalid cover type")
        self._cover_type = cover_type

    @property
    def get_available_cover_types(self) -> str:
        """returns all available textbook cover types in the library"""
        cover_type = '\n '.join(self.COVER_TYPE)
        return cover_type

    def suffix(self, val: int) -> str:
        """ determines the edition suffix sequence """
        suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
        return suffixes.get(val % 10, 'th')

    def to_dict(self) -> dict: # FIX_ME
        """returns textbook instance state as a dictionary"""
        instance = dict(id=self._book_id, title=self._book_title, author=self._author,
                        published_year=self._published_year, edition=self._edition,
                        cover_type=self._cover_type, subject=self._book_subject,
                        is_borrowed=self._is_borrowed)
        return instance

    def display_info(self) -> None:
        """displays the necessary book information using the attributes"""
        if self.get_availability_status():
            print(
                f'Book code {self.get_book_id} (BORROWED): {self.get_cover_type} {self.get_book_type} "{self.get_book_title}"'
                f' under the subject {self.get_book_subject}, {self.get_edition()}{self.suffix(self.get_edition())} edition'
                f' written by {self.get_author}, published in {self.get_published_year()}\n')
        else:
            print(
                f'Book code {self.get_book_id} (AVAILABLE): {self.get_cover_type} {self.get_book_type} "{self.get_book_title}"'
                f' under the subject {self.get_book_subject}, {self.get_edition()}{self.suffix(self.get_edition())} edition'
                f' written by {self.get_author}, published in {self.get_published_year()}\n')

    @classmethod
    def validate(cls, cover_type: str, book_subject: str) -> None:
        """validates the attributes of textbook object"""
        if type(cover_type) != str:
            raise TypeError(f'{cover_type} is invalid! Please enter the valid type of the textbook.')
        if cover_type not in cls.COVER_TYPE:
            raise ValueError(f'{cover_type} is not recognized as a standard cover type. '
                             f'The existing types are: {cls.get_available_cover_types}')
        if type(book_subject) != str:
            raise TypeError('Invalid subject! Please enter a valid book subject area. (e.g. math)')
        if book_subject.lower() not in cls.BOOK_SUBJECT:
            raise ValueError(f"no textbook under the subject {book_subject} exists.")
