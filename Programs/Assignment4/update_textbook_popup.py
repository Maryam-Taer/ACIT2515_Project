# Group 16
# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-04-08

import requests
from tkinter import ttk, messagebox as mb
from tkinter.ttk import Frame, Combobox, Label, Button, Style


class UpdateTextbookPopup(Frame):
    """ Popup Frame to Update a Textbook """

    def __init__(self, parent, book_id, close_callback):
        """ Constructor """
        Frame.__init__(self, parent)

        style = Style()
        style.configure('U.TButton', foreground='dark green', font=("TkTextFont", 11))
        style.configure('C.TButton', foreground='brown4', font=("TkTextFont", 11))
        style.configure('C.TLabel', foreground='purple4', font=("TkTextFont", 10, 'bold'))

        self._book_id = book_id
        self._close_cb = close_callback
        self.grid(padx=40, pady=40, rowspan=2, columnspan=2)

        Label(self, text="Cover Type:", style='C.TLabel').grid(row=2, column=1)
        self._cover_type = Combobox(self, values=['paperback', 'hardcover case wrap', 'hardcover dust jacket'])
        self._cover_type.current(0)
        self._cover_type.grid(row=2, column=2, padx=40, pady=10)

        Label(self, text="Book Subject:", style='C.TLabel').grid(row=3, column=1)
        self._subject = Combobox(self, values=['language', 'biology', 'health', 'english', 'french', 'arts',
                                               'music', 'science', 'psychology', 'math', 'poetry', 'history',
                                               'chemistry', 'physics', 'literature', 'short story'])
        self._subject.current(0)
        self._subject.grid(row=3, column=2, padx=40, pady=10)

        Button(self, text="Update", width=10, style='U.TButton', command=self._submit_cb).grid(row=4, column=1, padx=40, pady=10)
        Button(self, text="Cancel", width=10, style='C.TButton', command=self._close_cb).grid(row=4, column=2, padx=40)

    def _submit_cb(self):
        """ Submit the Update Textbook """
        data = {'cover_type': self._cover_type.get(), 'subject': self._subject.get()}

        response = requests.put(f"http://127.0.0.1:5000/library_manager/textbook/{self._book_id}", json=data)

        if response.status_code != 200:
            mb.showerror(title='Error while Submitting', message=response.text)
        else:
            self._close_cb()
            mb.showinfo('Update Successful', 'Textbook information was successfully updated.')
