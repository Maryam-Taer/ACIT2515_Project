# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-03-16

"""This program creates an object called 'InventoryStatus' to extract
the status of the added properties to the inventory. The three statuses
are to count the number of sold properties, the number of properties for sale,
and the total profit from all the sold properties."""


class LibraryStats:
    """ initiates the statistics a book record """

    def __init__(self, num_not_borrowed, num_borrowed, num_textbooks, num_ebooks):

        self._num_not_borrowed = num_not_borrowed
        self.validate(num_not_borrowed, 'borrowed books')

        self._num_borrowed = num_borrowed
        self.validate(num_borrowed, 'borrowed books')

        self._num_textbooks = num_textbooks
        self.validate(num_textbooks, 'number of textbooks')

        self._num_ebooks = num_ebooks
        self.validate(num_ebooks, 'number of eBooks')

    def validate(self, attribute, value, min_value=0) -> None:
        """validation of book statuses"""
        error_message = f"Invalid value: {value}."
        if attribute is None:
            raise ValueError(error_message)
        if type(attribute) != int:
            raise ValueError(error_message)
        if attribute < min_value:
            raise ValueError(error_message)

    def to_dict(self):
        """ returns book instance stats as dictionary """
        stat = dict()
        stat["Number of books not borrowed"] = self._num_not_borrowed
        stat["Number of books borrowed"] = self._num_borrowed
        stat["Number of textbooks"] = self._num_textbooks
        stat["Number of ebooks"] = self._num_ebooks
        return stat

    def get_num_not_borrowed(self) -> int:
        """ returns the number books that are available for the customer to borrow"""
        return self._num_not_borrowed

    def get_num_borrowed(self) -> int:
        """ returns the number books that are already borrowed"""
        return self._num_borrowed

    def get_num_textbooks(self) -> int:
        """ returns the number of textbooks"""
        return self._num_textbooks

    def get_num_ebooks(self) -> int:
        """ returns the number of ebooks"""
        return self._num_ebooks
