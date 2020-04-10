# Group 16
# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-04-08

import requests
from tkinter import messagebox as mb, StringVar
from tkinter.ttk import Frame, Combobox, Label, Button, Style


class UpdateeBookPopup(Frame):
    """ Popup Frame to Update an eBook """

    def __init__(self, parent, book_id, close_callback):
        """ Constructor """
        Frame.__init__(self, parent)

        style = Style()
        style.configure('U.TButton', foreground='dark green', font=("TkTextFont", 11))
        style.configure('C.TButton', foreground='brown4', font=("TkTextFont", 11))
        style.configure('C.TLabel', foreground='purple4', font=("TkTextFont", 10, 'bold'))

        self._close_cb = close_callback
        self.grid(padx=40, pady=40, rowspan=2, columnspan=2)

        self._book_id = book_id

        Label(self, text="Platform:", style='C.TLabel').grid(row=2, column=1)
        self._platform = Combobox(self, textvariable=StringVar(), values=["OverDrive Read", "Fast Read ebooks"])
        self._platform.current(0)
        self._platform.grid(row=2, column=2, padx=40, pady=10)

        Label(self, text="Genre:", style='C.TLabel').grid(row=3, column=1)
        self._genre = Combobox(self, textvariable=StringVar(), values=['biography', 'kids', 'business & finance',
                                                                       'romance', 'mystery', 'comics', 'fantasy',
                                                                       'notification', 'literature', 'periodicals'])
        self._genre.current(0)
        self._genre.grid(row=3, column=2, padx=40, pady=10)

        Button(self, text="Update", width=15, style='U.TButton', command=self._submit_cb).grid(row=4, column=1, padx=40, pady=10)
        Button(self, text="Cancel", width=15, style='C.TButton', command=self._close_cb).grid(row=4, column=2, padx=40)

    def _submit_cb(self):
        """ Submit the Update eBook """
        data = {'platform': self._platform.get(), 'genre': self._genre.get()}

        response = requests.put(f"http://127.0.0.1:5000/library_manager/ebook/{self._book_id}", json=data)

        if response.status_code != 200:
            mb.showerror(title='Error while Submitting', message=response.text)
        else:
            self._close_cb()
            mb.showinfo('Update Successful', 'eBook information was successfully updated.')
