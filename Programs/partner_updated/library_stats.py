

class LibraryStats:


    def __init__(self, num_not_borrowed, num_borrowed, num_textbooks, num_ebooks):
        self._num_not_borrowed = num_not_borrowed
        self._num_borrowed = num_borrowed
        self._num_textbooks = num_textbooks
        self._num_ebooks = num_ebooks


    def get_num_not_borrowed(self):
        return self._num_not_borrowed


    def get_num_borrowed(self):
        return self._num_borrowed


    def get_num_textbooks(self):
        return self._num_textbooks


    def get_num_ebooks(self):
        return self._num_ebooks