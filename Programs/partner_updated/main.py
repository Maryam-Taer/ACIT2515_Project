

from textbook import Textbook
from ebook import eBook
from library_manager import LibraryManager


if __name__ == '__main__':
    book1 = Textbook('111', 'hunger games', 'john', 1111, 2, False, 'subject')
    book2 = Textbook('222', 'hunger games', 'john', 1111, 2, False, 'subject')
    book3 = eBook('222', 'hunger games', 'john', 1111, 2, False, 'subject')


    library = LibraryManager('library')

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print(book1.get_type())


    print(book2.display_info())

    # library.remove_book('111')
    print(library.get_book_by_id('111'), 'getting book by id')
    print(library.get_book_by_id('222'), 'getting book by id')

    print(library.exists_in_library('111'))

    print(library.available_in_library('111'))

    print(library.get_all(), 'getting all')

    print(library.get_all_by_type('ebook'), 'getting all by ebook')
    print(library.get_all_by_type('textbook'), 'getting all by textbook')


    print(library.get_book_stat())

    print()
    print()

    stats = library.get_book_stat()
    print("stats for", library.get_name())
    print(f"  # of books borrowed: {stats.get_num_borrowed():d}")
    print(f"  # of books available: {stats.get_num_not_borrowed():d}")
    print(f"  # of textbooks: {stats.get_num_textbooks():d}")
    print(f"  # of ebooks: {stats.get_num_ebooks():d}")
