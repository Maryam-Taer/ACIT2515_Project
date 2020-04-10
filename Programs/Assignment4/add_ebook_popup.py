# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-04-08

import re
import requests
from tkinter import ttk, messagebox as mb, StringVar
from tkinter.ttk import Style


class AddeBookPopup(ttk.Frame):
    """ Popup Frame to Add a Student """

    def __init__(self, parent, close_callback):
        """ Constructor """
        ttk.Frame.__init__(self, parent)

        style = Style()
        style.configure('S.TButton', foreground='dark green', font=("TkTextFont", 11))
        style.configure('C.TButton', foreground='brown4', font=("TkTextFont", 11))
        style.configure('C.TLabel', foreground='purple4', font=("TkTextFont", 10, 'bold'))

        self._close_cb = close_callback
        self.grid(padx=40, pady=40, rowspan=2, columnspan=2)

        ttk.Label(self, text="Book ID:", style='C.TLabel').grid(row=1, column=1)
        self._book_id = ttk.Entry(self)
        self._book_id.grid(row=1, column=2, padx=40, pady=10)

        ttk.Label(self, text="Title:", style='C.TLabel').grid(row=2, column=1)
        self._title = ttk.Entry(self)
        self._title.grid(row=2, column=2, padx=40, pady=10)

        ttk.Label(self, text="Author:", style='C.TLabel').grid(row=3, column=1)
        self._author = ttk.Entry(self)
        self._author.grid(row=3, column=2, padx=40, pady=10)

        ttk.Label(self, text="Year Published:", style='C.TLabel').grid(row=4, column=1)
        self._published_year = ttk.Entry(self)
        self._published_year.grid(row=4, column=2, padx=40, pady=10)

        ttk.Label(self, text="Edition:", style='C.TLabel').grid(row=5, column=1)
        self._edition = ttk.Entry(self)
        self._edition.grid(row=5, column=2, padx=40, pady=10)

        ttk.Label(self, text="Platform:", style='C.TLabel').grid(row=6, column=1)
        self._platform = ttk.Combobox(self, textvariable=StringVar(), values=["OverDrive Read", "Fast Read ebooks"])
        self._platform.current(0)
        self._platform.grid(row=6, column=2, padx=40, pady=10)

        ttk.Label(self, text="Genre:", style='C.TLabel').grid(row=7, column=1)
        self._genre = ttk.Combobox(self, textvariable=StringVar(), values=['biography', 'kids', 'business & finance',
                                                                           'romance', 'mystery', 'comics', 'fantasy',
                                                                           'notification', 'literature', 'periodicals'])
        self._genre.current(0)
        self._genre.grid(row=7, column=2, padx=40, pady=10)

        ttk.Button(self, text="Add", width=15, style="S.TButton", command=self._validate_entry).grid(row=8, column=1, padx=40, pady=10)
        ttk.Button(self, text="Cancel", width=15, style="C.TButton", command=self._close_cb).grid(row=8, column=2, padx=40)

    def _submit_cb(self):
        """ Submit the Add Student """
        data = {'book_id': self._book_id.get(),
                'title': self._title.get(),
                'author': self._author.get(),
                'published_year': self._published_year.get(),
                'edition': self._edition.get(),
                'platform': self._platform.get(),
                'genre': self._genre.get()}

        response = requests.post("http://127.0.0.1:5000/library_manager/ebook", json=data)

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




