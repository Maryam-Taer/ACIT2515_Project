

from textbook import Textbook
from library_manager import LibraryManager


if __name__ == '__main__':
    book1 = Textbook('111', 'hunger games', 'john', 1111, 2, False, 'u', 'i')
    book2 = Textbook('222', 'hunger games', 'john', 1111, 2, True, 'u', 'i')
    # print(book1.get_edition())
    # print(book1.display_info())

    library = LibraryManager('library')
    # print(library.get_name())
    library.add_book(book1)
    library.add_book(book2)
    # print(library.get_book_by_id('222'))
    # library.remove_book(book2)
    # print(library.get_inventory())
    # print(library.get_book_by_id('111'))
    # print(library.get_book_by_id('222'))

    # print(library.exists_in_library('222'))

    library.available_books('222')
    library.available_books('111')