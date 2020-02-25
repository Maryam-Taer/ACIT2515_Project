

from library_stats import LibraryStats


class LibraryManager:
    def __init__(self, name):
        self._name = name
        self._inventory = []

    def get_name(self):
        return self._name

    def add_book(self, book):
        try:
            # if book._is_borrowed is True:
            #     print('book is already borrowed')
            # else:
            self._inventory.append(book)
        except NameError:
            print(book, 'does not exist')
        except AttributeError:
            print(book, 'is not right attribute')

    def remove_book(self, book_id):
        try:
            for i in self._inventory:
                if i.get_id() == book_id:
                    self._inventory.remove(i)
        except NameError:
            print(book_id, 'does not exist')
        except AttributeError:
            print(book_id, 'is not an object')
        except TypeError:
            print('missing requirements, or too many')

    def get_book_by_id(self, id):
        try:
            for i in self._inventory:
                if i.get_id() == id:
                    return i
        except KeyError:
            print(id, 'does not exist')

    def get_all(self):
        list = []
        for i in self._inventory:
            list.append(i)
        return list

    def get_all_by_type(self, type):
        list = []
        for i in self._inventory:
            if i.get_type() == type:
                list.append(i)
        return list


    def get_inventory(self):
        return self._inventory

    def exists_in_library(self, id):
        try:
            for i in self._inventory:
                if i.get_id() == id:
                    return True
                else:
                    return False
        except NameError:
            print(id, 'does not exist')

    def available_in_library(self, id):
        """checks if the book is available"""
        for i in self._inventory:
            if i.get_id() == id:
                if i.get_availabilty_status() == True:
                    return True
                else:
                    return False


    def get_book_stat(self):
        num_borrowed = 0
        num_not_borrowed = 0
        num_textbook = 0
        num_ebook = 0
        for i in self._inventory:
            if i.get_availabilty_status() is True:
                num_borrowed += 1
            if i.get_availabilty_status() is False:
                num_not_borrowed += 1
            if i.get_type() == 'textbook':
                num_textbook += 1
            if i.get_type() == 'ebook':
                num_ebook += 1
        return LibraryStats(num_not_borrowed, num_borrowed, num_textbook, num_ebook)





