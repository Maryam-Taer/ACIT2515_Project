# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-03-16

"""This is the child class of 'Book' class that inherits common attributes
initiated in the 'Book' class while specifying its own attributes that
distinguishes a 'eBook' with other type of books"""

from book import Book


class eBook(Book):
    BOOK_TYPE = 'ebook'
    PLATFORM = ['OverDrive Read', 'Fast Read Ebooks']
    BOOK_GENRE = ['biography', 'kids', 'business & finance', 'romance',
                  'mystery', 'comics', 'fantasy', 'notification', 'literature', 'periodicals']

    """initiates all the special attributes of a book as well as inheriting the common attributes"""

    def __init__(self, book_id, book_title, author, published_year, edition, platform, book_genre, is_borrowed):
        super().__init__(book_id, book_title, author, published_year, edition, is_borrowed)
        self._platform = platform
        self._book_genre = book_genre
        self.validate(platform, book_genre)

    @property
    def get_book_type(self) -> str:
        """returns the type of the book"""
        return self.BOOK_TYPE

    @property
    def get_book_platform(self) -> str:
        """returns the eBook platforms"""
        return self._platform

    def set_book_platform(self, platform: str) -> None:
        """sets the eBook platform"""
        if type(platform) is not str:
            raise TypeError("Invalid platform")
        if platform not in self.PLATFORM:
            raise ValueError("Invalid platform")
        self._platform = platform

    @property
    def get_available_platforms(self) -> str:
        """returns the available platforms in the library that the ebook can run on"""
        platform = '\n '.join(self.PLATFORM)
        return platform

    @property
    def get_book_genre(self) -> str:
        """returns the eBook category"""
        return self._book_genre

    def set_book_genre(self, genre: str) -> None:
        """sets the eBook genre"""
        if type(genre) is not str:
            raise TypeError("Invalid subject")
        if genre not in self.BOOK_GENRE:
            raise ValueError("Invalid subject")
        self._book_genre = genre

    def suffix(self, val: int) -> str:
        """determines the edition suffix sequence"""
        suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
        return suffixes.get(val % 10, 'th')

    def to_dict(self) -> dict:
        """returns ebook instance state as a dictionary"""
        instance = dict(id=self._book_id, title=self._book_title, author=self._author,
                        published_year=self._published_year, edition=self._edition,
                        platform=self._platform, genre=self._book_genre,
                        is_borrowed=self._is_borrowed)
        return instance

    @classmethod
    def validate(cls, platform: str, book_category: str) -> None:
        """validates the attributes of textbook object"""
        if type(platform) != str:
            raise TypeError(f'{platform} is invalid! Please enter the valid type of the eBook platform.')
        if platform not in cls.PLATFORM:
            raise ValueError(f'{platform} is not recognized as a standard platform. The existing types are: '
                             f'{cls.get_available_platforms}')
        if type(book_category) != str:
            raise TypeError('Invalid subject! Please enter a valid book genre. (e.g. fiction)')
        if book_category.lower() not in cls.BOOK_GENRE:
            raise ValueError(f'no textbook under the subject {book_category} exists.')

    def display_info(self):
        """displays the necessary book information using the attributes"""
        if self.get_availability_status():
            print(
                f'Book code {self.get_book_id} (BORROWED): {self.get_book_genre} {self.get_book_type} "{self.get_book_title}"'
                f' running on {self.get_book_platform}, {self.get_edition()}{self.suffix(self.get_edition())} edition'
                f' written by {self.get_author}, published in {self.get_published_year()}\n')
        else:
            print(
                f'Book code {self.get_book_id} (AVAILABLE): {self.get_book_genre} {self.get_book_type} "{self.get_book_title}"'
                f' running on {self.get_book_genre}, {self.get_edition()}{self.suffix(self.get_edition())} edition'
                f' written by {self.get_author}, published in {self.get_published_year()}\n')
