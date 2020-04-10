# Group 16
# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-04-08

import re
import requests
import tkinter as tk
from tkinter import ttk, messagebox as mb
from tkinter.ttk import Style, Frame, Label, Button, Entry


class DeleteBook(Frame):
    """ Popup Frame to delete a book """

    def __init__(self, parent, close_callback):
        """ Constructor """

        Frame.__init__(self, parent)

        style = Style()
        style.configure('D.TButton', foreground='Brown4', font=("TkTextFont", 9))

        self._close_cb = close_callback

        self.grid(padx=30, pady=30, rowspan=2, columnspan=2)

        Label(self, text="Book ID:").grid(row=2, column=1, padx=10, pady=10)
        self._book_id = Entry(self)
        self._book_id.grid(row=2, column=2, padx=10, pady=10)
        Button(self, text="Delete", width=15, style='D.TButton', command=self._validate_id).grid(row=4, column=1, padx=10, pady=10)
        Button(self, text="Cancel", width=15, command=self._close_cb).grid(row=4, column=2, padx=30)

    def _delete_confirmation(self):
        """ Delete confirmation Message Box """
        answer = mb.askyesno('Verify', 'Are you sure you want to delete this book?')
        if answer:
            self._delete_cb()

    def _delete_cb(self):
        """ Submit the delete book """
        response = requests.delete(f"http://127.0.0.1:5000/library_manager/book/{self._book_id.get()}")

        if response.status_code != 200:
            tk.Label(self, text=response.text).grid(row=3, column=1)
        else:
            self._close_cb()

    def _validate_id(self):
        """ Book ID validation """
        book_id = self._book_id.get()
        if (not (2 < len(book_id) < 7)) or (not type(book_id) == str):
            tk.Label(self, text=f'Invalid Book ID "{book_id}"').grid(row=3, column=1)
        else:
            self._delete_confirmation()
