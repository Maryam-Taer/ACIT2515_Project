# Group 16
# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-04-08

"""This program creates an object called 'InventoryStatus' to extract
the status of the added properties to the inventory. The three statuses
are to count the number of sold properties, the number of properties for sale,
and the total profit from all the sold properties."""


class LibraryStats:
    """ initiates the statistics a book record """

    def __init__(self, num_ebooks, num_textbooks, num_books, borrowed_ebooks, borrowed_textbooks, borrowed_books):

        self._num_ebooks = num_ebooks
        self.validate(num_ebooks, 'number of eBooks')

        self._num_textbooks = num_textbooks
        self.validate(num_textbooks, 'number of textbooks')

        self._num_books = num_books
        self.validate(num_books, 'number of books')

        self._borrowed_ebooks = borrowed_ebooks
        self.validate(borrowed_ebooks, 'borrowed ebooks')

        self._borrowed_textbooks = borrowed_textbooks
        self.validate(borrowed_textbooks, 'borrowed textbooks')

        self._borrowed_books = borrowed_books
        self.validate(borrowed_books, 'borrowed Books')

    def validate(self, attribute, value, min_value=0) -> None:
        """ validation of book statuses """
        error_message = f"Invalid value: {value}."
        if attribute is None:
            raise ValueError(error_message)
        if type(attribute) != int:
            raise ValueError(error_message)
        if attribute < min_value:
            raise ValueError(error_message)

    def to_dict(self):
        """ Return book instance stats as dictionary """
        stat = {'eBooks ': self._num_ebooks,
                'Textbooks ': self._num_textbooks,
                'All Books ': self._num_books,
                'Borrowed eBooks ': self._borrowed_ebooks,
                'Borrowed Textbooks ': self._borrowed_textbooks,
                'All Borrowed Books ': self._borrowed_books}
        return stat

    def get_num_ebooks(self) -> int:
        """ Return the number of ebooks"""
        return self._num_ebooks

    def get_num_textbooks(self) -> int:
        """ Return the number of textbooks"""
        return self._num_textbooks

    def get_num_books(self) -> int:
        """ Return the number of textbooks"""
        return self._num_books

    def get_borrowed_ebook(self) -> int:
        """ Return the number books that are available for the customer to borrow"""
        return self._borrowed_ebooks

    def get_borrowed_textbook(self) -> int:
        """ Return the number books that are already borrowed"""
        return self._borrowed_textbooks

    def get_borrowed_books(self) -> int:
        """ Return the number of textbooks"""
        return self._borrowed_books
