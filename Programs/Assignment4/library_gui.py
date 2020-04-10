# Group 16
# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-04-08

import requests
import tkinter as tk
from ttkthemes import themed_tk
from tkinter import messagebox as mb, StringVar, Listbox, Text
from tkinter.ttk import Style, OptionMenu, Frame, Button, Label
from add_ebook_popup import AddeBookPopup
from add_textbook_popup import AddTextbookPopup
from update_ebook_popup import UpdateeBookPopup
from update_textbook_popup import UpdateTextbookPopup
from delete_book import DeleteBook


class MainAppController(Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        Frame.__init__(self, parent)

        # create a style object
        style = Style()
        style.configure('D.TButton', foreground='red3')
        style.configure('R.TButton', foreground='DodgerBlue4', font=("TkTextFont", 9, 'bold'))
        style.configure('B.TButton', foreground='FireBrick4', font=("TkTextFont", 9, 'bold'))

        # Left frame, column 1
        left_frame = Frame(master=self)
        left_frame.grid(row=1, column=1, padx=30, pady=35, rowspan=3)

        # Middle frame (info text, column 2)
        middle_frame = Frame(master=self)
        middle_frame.grid(row=1, column=2, padx=30, pady=35, rowspan=3)

        # Right frame (statistics, column 3)
        right_frame = Frame(master=self)
        right_frame.grid(row=1, column=3, padx=30, pady=35, rowspan=2)

        # LEFT FRAME WIDGET
        Label(left_frame, text="Book ID", font=("TkTextFont", 11)).grid(row=1, column=1, columnspan=3)
        self._book_list = Listbox(left_frame, height=10, width=10, font=("TkTextFont", 11), bg='LightSalmon2')
        self._book_list.grid(row=2, column=1)
        self._book_list.configure(justify="center")

        # Call this on select
        self._book_list.bind("<<ListboxSelect>>", self._update_textbox)

        # MIDDLE FRAME WIDGET
        Label(middle_frame, text="Book Summary", font=("TkTextFont", 11)).grid(row=1, column=2, columnspan=7)
        self._info_text = Text(master=middle_frame, height=10, width=45, font=("TkTextFont", 11), bg='plum2')
        self._info_text.grid(row=2, column=2, columnspan=7)
        self._info_text.tag_configure("bold", font=("TkTextFont", 10, "bold"))

        # RIGHT FRAME WIDGET
        Label(right_frame, text="Book Statistics", font=("TkTextFont", 11)).grid(row=1, column=1, columnspan=3)
        self._book_stat = Text(master=right_frame, height=10.5, width=30, font=("TkTextFont", 10), bg='LightSalmon2')
        self._book_stat.grid(row=2, column=1, rowspan=3)
        self._book_stat.tag_configure("bold", font=("TkTextFont", 10, "bold"))

        # Drop Down menu to add a book
        self._add_var = StringVar(left_frame)
        choices = ['eBook', 'Textbook']
        OptionMenu(middle_frame, self._add_var, 'Select Type', *choices).grid(row=3, column=2, pady=5, columnspan=4)

        # Drop Down menu to update a book
        self._update_var = StringVar(left_frame)
        choices = ['eBook', 'Textbook']
        OptionMenu(middle_frame, self._update_var, 'Select Type', *choices).grid(row=3, column=3, pady=5, columnspan=7)

        # A couple buttons - using TTK
        Button(left_frame, text="Delete Book", width=13, command=self._delete_book, style='D.TButton').grid(row=3, column=1, pady=5)
        Button(left_frame, text="Quit", width=13, command=self._quit_callback).grid(row=4, column=1)
        Button(middle_frame, text="Add Book", width=13, command=self._add_book).grid(row=4, column=2, columnspan=4)
        Button(middle_frame, text="Update Book", width=13, command=self._update_book).grid(row=4, column=3, columnspan=7)
        Button(right_frame, text="Borrow Book", width=13, command=self._borrow_cb, style='B.TButton').grid(row=5, column=1, pady=5)
        Button(right_frame, text="Return Book", width=13, command=self._return_cb, style='R.TButton').grid(row=6, column=1)

        # Now update the list and Statistics
        self._update_book_list()

    def _update_textbox(self, *args):
        """ Updates the info text box on the right, based on the current ID selected """
        # This is a list, so we take just the first item (could be multi select...)
        try:
            selected_index = self._book_list.curselection()[0]
        except IndexError:
            return None
        book_id = self._book_list.get(selected_index)

        # Make a GET request
        r = requests.get(f"http://localhost:5000/library_manager/book/{book_id}")

        # Clear the text box
        self._info_text.delete(1.0, tk.END)

        # Check the request status code
        if r.status_code != 200:
            self._info_text.insert(tk.END, "Error running the request!")

        # For every item (key, value) in the JSON response, display them:
        for k, v in r.json().items():
            self._info_text.insert(tk.END, f"{k.capitalize()}\t\t", "bold")
            self._info_text.insert(tk.END, f"{v}\n")

        self._update_book_stat()

    def _update_book_list(self):
        """ Update the List of Books """
        r = requests.get("http://localhost:5000/library_manager/all")
        self._book_list.delete(0, tk.END)
        for s in r.json()["ebook"]:
            self._book_list.insert(tk.END, '{:^}'.format(s['book_id']))
            self._book_list.itemconfig(tk.END, {'fg': 'Blue4'})
            if s['is_borrowed']:
                self._book_list.itemconfig(tk.END, {'bg': 'khaki1'})

        for s in r.json()["textbook"]:
            self._book_list.insert(tk.END, '{:^}'.format(s['book_id']))
            self._book_list.itemconfig(tk.END, {'fg': 'Brown4'})
            if s['is_borrowed']:
                self._book_list.itemconfig(tk.END, {'bg': 'khaki1'})
        self._update_book_stat()

    def _update_book_stat(self):
        """ Update the List of Books """
        r = requests.get("http://localhost:5000/library_manager/all/stats")
        self._book_stat.delete(1.0, tk.END)
        for k, v in r.json().items():
            self._book_stat.insert(tk.END, f"{k}\t\t\t", "bold")
            self._book_stat.insert(tk.END, f"{v}\n")

    def _borrow_cb(self):
        """Borrow any book with the selected ID"""
        if not self._book_list.curselection():
            mb.showerror('Error : Item not selected', 'Please select a book.')
        else:
            selected_index = self._book_list.curselection()[0]
            book_id = self._book_list.get(selected_index)
            r = requests.get(f"http://127.0.0.1:5000/library_manager/book/{book_id}")
            if r.json()['is_borrowed']:
                mb.showerror('Error : Bad selection', 'Book is already borrowed.')
            else:
                response = requests.put(f"http://127.0.0.1:5000/library_manager/{book_id}/borrow")
                if response.status_code == 200:
                    self._update_book_list()

    def _return_cb(self):
        """Return any book with the selected ID to library"""
        if not self._book_list.curselection():
            mb.showerror('Error : Item not selected', 'Please select a book.')
        else:
            selected_index = self._book_list.curselection()[0]
            book_id = self._book_list.get(selected_index)
            r = requests.get(f"http://127.0.0.1:5000/library_manager/book/{book_id}")
            if not r.json()['is_borrowed']:
                mb.showerror('Error : Bad selection', 'Book is already returned.')
            else:
                response = requests.put(f"http://127.0.0.1:5000/library_manager/{book_id}/return_book")
                if response.status_code == 200:
                    self._update_book_list()

    def _add_ebook(self):
        """ Add eBook Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddeBookPopup(self._popup_win, self._close_book_cb)

    def _add_textbook(self):
        """ Add Textbook Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddTextbookPopup(self._popup_win, self._close_book_cb)

    def _add_book(self):
        """Redirect add book based on the type"""
        if self._add_var.get() == 'eBook':
            self._add_ebook()
        elif self._add_var.get() == 'Textbook':
            self._add_textbook()
        else:
            mb.showerror('Error : Type not selected', 'Please select a type.')

    def _update_book(self):
        """Update eBook attributes"""
        if self._update_var.get() == 'eBook':
            self._update_ebook()
        elif self._update_var.get() == 'Textbook':
            self._update_textbook()
        else:
            mb.showerror('Error : Type not selected', 'Please select a type.')

    def _update_ebook(self):
        """Update ebook attributes in the 'Book' database"""
        if not self._book_list.curselection():
            mb.showerror('Error : Book not selected', 'Please select a book.')
        else:
            selected_index = self._book_list.curselection()[0]
            book_id = self._book_list.get(selected_index)
            r = requests.get(f"http://localhost:5000/library_manager/book/{book_id}")
            if r.json()['type'] != 'ebook':
                mb.showerror('Error : Invalid selection', 'Please select an ebook ID.')
            else:
                self._popup_win = tk.Toplevel()
                self._popup = UpdateeBookPopup(self._popup_win, book_id, self._close_book_cb)
        self._update_book_list()

    def _update_textbook(self):
        """Update textbook attributes in the 'Book' database"""
        if not self._book_list.curselection():
            mb.showerror('Error : Book not selected', 'Please select a book.')
        else:
            self._popup_win = tk.Toplevel()
            selected_index = self._book_list.curselection()[0]
            book_id = self._book_list.get(selected_index)
            r = requests.get(f"http://localhost:5000/library_manager/book/{book_id}")
            if r.json()['type'] != 'textbook':
                mb.showerror('Error : Invalid selection', 'Please select a textbook ID.')
            else:
                self._popup = UpdateTextbookPopup(self._popup_win, book_id, self._close_book_cb)
        self._update_book_list()

    def _delete_book(self):
        """ Delete book Popup """
        self._popup_win = tk.Toplevel()
        self._popup = DeleteBook(self._popup_win, self._close_book_cb)

    def _close_book_cb(self):
        """ Close Popup """
        self._popup_win.destroy()
        self._update_book_list()

    def _quit_callback(self):
        """ Quit """
        self.quit()


if __name__ == "__main__":
    root = themed_tk.ThemedTk()
    root.title('Library Management System')
    root.get_themes()
    root.set_theme('scidpurple')
    root.geometry("850x340")
    MainAppController(root).pack()
    root.mainloop()
