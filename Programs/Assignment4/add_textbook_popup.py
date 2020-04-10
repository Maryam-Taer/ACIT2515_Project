# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-04-08

import re
import requests
from tkinter import messagebox as mb
from tkinter.ttk import Style, Frame, Label, Button, Entry, Combobox


class AddTextbookPopup(Frame):
    """ Popup Frame to Add a Student """

    def __init__(self, parent, close_callback):
        """ Constructor """
        Frame.__init__(self, parent)

        style = Style()
        style.configure('S.TButton', foreground='dark green', font=("TkTextFont", 11))
        style.configure('C.TButton', foreground='brown4', font=("TkTextFont", 11))
        style.configure('C.TLabel', foreground='purple4', font=("TkTextFont", 10, 'bold'))

        self._close_cb = close_callback
        self.grid(padx=40, pady=40, rowspan=2, columnspan=2)

        Label(self, text="Book ID:", style='C.TLabel').grid(row=1, column=1)
        self._book_id = Entry(self)
        self._book_id.grid(row=1, column=2, padx=40, pady=10)

        Label(self, text="Title:", style='C.TLabel').grid(row=2, column=1)
        self._title = Entry(self)
        self._title.grid(row=2, column=2, padx=40, pady=10)

        Label(self, text="Author:", style='C.TLabel').grid(row=3, column=1)
        self._author = Entry(self)
        self._author.grid(row=3, column=2, padx=40, pady=10)

        Label(self, text="Year Published:", style='C.TLabel').grid(row=4, column=1)
        self._published_year = Entry(self)
        self._published_year.grid(row=4, column=2, padx=40, pady=10)

        Label(self, text="Edition:", style='C.TLabel').grid(row=5, column=1)
        self._edition = Entry(self)
        self._edition.grid(row=5, column=2, padx=40, pady=10)

        Label(self, text="Cover Type:", style='C.TLabel').grid(row=6, column=1)
        self._cover_type = Combobox(self, values=['paperback', 'hardcover case wrap', 'hardcover dust jacket'])
        self._cover_type.current(0)
        self._cover_type.grid(row=6, column=2, padx=40, pady=10)

        Label(self, text="Book Subject:", style='C.TLabel').grid(row=7, column=1)
        self._subject = Combobox(self, values=['language', 'biology', 'health', 'english', 'french', 'arts',
                                               'music', 'science', 'psychology', 'math', 'poetry', 'history',
                                               'chemistry', 'physics', 'literature', 'short story'])
        self._subject.current(0)
        self._subject.grid(row=7, column=2, padx=40, pady=10)

        Button(self, text="Add", width=15, style="S.TButton", command=self._validate_entry).grid(row=8, column=1,
                                                                                                 padx=40, pady=10)
        Button(self, text="Cancel", width=15, style="C.TButton", command=self._close_cb).grid(row=8, column=2, padx=40)

    def _submit_cb(self):
        """ Submit the Add Student """
        data = {'book_id': self._book_id.get(),
                'title': self._title.get(),
                'author': self._author.get(),
                'published_year': self._published_year.get(),
                'edition': self._edition.get(),
                'cover_type': self._cover_type.get(),
                'subject': self._subject.get()}

        response = requests.post("http://127.0.0.1:5000/library_manager/textbook", json=data)

        if response.status_code != 200:
            mb.showerror(title='Error while Submitting', message=response.text)
        else:
            self._close_cb()

    def _validate_entry(self):
        """Entry Validation"""
        book_id = self._book_id.get()
        title = self._title.get()
        author = self._author.get()
        published_year = self._published_year.get()
        edition = self._edition.get()

        # if not (book_id or title or author or published_year or edition) DOESN'T work for me :)
        # Also I tried regex and for some reason that didn't work either

        if (not book_id) or (not title) or (not author) or (not published_year) or (not edition):
            mb.showerror(title='Error while Submitting', message='Please fill all fields.')

        elif (not type(book_id) == str) or (not (2 < len(book_id) < 7)):
            mb.showerror(title='Error while Submitting', message='Please enter a valid ID.')

        elif (not int(published_year)) or (not (1920 < int(published_year) < 2020)):
            mb.showerror(title='Error while Submitting', message='Please enter a valid year.')

        elif (not int(edition)) or (not int(edition) > 1):
            mb.showerror(title='Error while Submitting', message='Please enter a valid edition.')

        else:
            self._submit_cb()
