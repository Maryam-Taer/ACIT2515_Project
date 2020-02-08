






class LibraryManager:
    def __init__(self, name):
        self._name = name
        self._inventory = {}


    def get_name(self):
        return self._name


    def add_book(self, book):
        self._inventory[book._book_id] = book.display_info()


    def remove_book(self, book):
        del self._inventory[book._book_id]


    def get_book_by_id(self, id):
        return self._inventory[id]


    def get_inventory(self):
        return self._inventory



    def exists_in_library(self, id):
        if id in self._inventory:
            return True
        else:
            return False





    def available_books(self, id):
        """checks if the book is available"""
        if id in self._inventory:
            if self._inventory[id][5] is True:
                print(self._inventory[id])
            else:
                print('not available')
        else:
            print(id, 'does not exist in inventory')




