# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-02-20

"""creating instances and validation of the methods happens here"""

from textbook import Textbook
from ebook import eBook
from library_manager import LibraryManager


def print_report(library):
    """This method runs some test on the created objects to validate
    the performance of the methods"""
    book_stat = library.get_book_stat()

    print(f" Librarian {library.get_name}")
    print(f"\tNumber of ebooks in the library: {book_stat.get_num_ebooks():d}")
    print(f"\tNumber of textbooks in the library: {book_stat.get_num_textbooks():d}")
    print(f"\tNumber of books borrowed: {book_stat.get_num_borrowed():d}")
    print(f"\tNumber of books available to borrow: {book_stat.get_num_not_borrowed():d}\n")
    print('ebooks available to borrow:')
    librarian.show_book_not_borrowed('ebook')
    print('Textbooks available to borrow:')
    librarian.show_book_not_borrowed('textbook')

    # print('ebook genres available in the library:')
    # librarian.show_available_book_category('ebook')
    # print('Textbook subjects available in the library:')
    # librarian.show_available_book_category('textbook')


if __name__ == '__main__':
    librarian = LibraryManager('Susan Sanderson')
    book1 = Textbook('A111', 'why do we need to sleep?', 'John Simpliciano', 2017, 3, 'hardcover case wrap', 'health', False)
    book2 = Textbook('B222', 'color methology', 'Maryam Taer', 2002, 4, 'paperback', 'arts', True)
    book3 = Textbook('V654', 'Hamlet', 'Shakespeare', 2000, 10, 'hardcover dust jacket', 'literature', True)
    book4 = Textbook('F009', 'Mein Kampf', 'Adolf Hitler', 1925, 6, 'paperback', 'history', False)
    book5 = eBook('B20V2', 'Me', 'Elton John', 2017, 4, 'OverDrive Read', 'biography', False)
    book6 = eBook('M3K12', 'Pax', 'Sara Pennypacker', 2012, 5, 'OverDrive Read', 'kids', True)
    book7 = eBook('L091A', 'Deadpool Vol.4: Monkey Business', 'Daniel Way', 2019, 5, 'Fast Read Ebooks', 'comics', True)
    book8 = eBook('GH255', 'Golden in Death', 'J. D Robb', 2016, 5, 'OverDrive Read', 'fantasy', True)
# ----------------------------------------------------------------------------------------------------------------------

    """Trying some 'success' cases per method"""
    try:
        librarian.add_book(book1)
    except LookupError:
        print('The property already exists in the inventory.')

    try:
        librarian.add_book(book2)
    except LookupError:
        print('The property already exists in the inventory.')

    try:
        librarian.add_book(book3)
    except LookupError:
        print('The property already exists in the inventory.')

    try:
        librarian.add_book(book4)
    except LookupError:
        print('The property already exists in the inventory.')

    try:
        librarian.add_book(book5)
    except LookupError:
        print('The property already exists in the inventory.')

    try:
        librarian.add_book(book6)
    except LookupError:
        print('The property already exists in the inventory.')

    try:
        librarian.add_book(book7)
    except LookupError:
        print('The property already exists in the inventory.')

    try:
        librarian.add_book(book8)
    except LookupError:
        print('The property already exists in the inventory.')

    # print_report(librarian)
    # print(librarian.exists_in_library('A111'))
    # librarian.remove_book('A111')
    # print(librarian.exists_in_library('A111'))
    # print(librarian.get_all_books())

    # print(librarian.get_books_by_type("textbook"))
    # print(book1.to_dict())
    # librarian._read_from_file('library_Manager.json')
    # print(librarian.write_to_file())

