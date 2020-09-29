# ACIT2515 Assignment - Group 16 - John Simpliciano & Maryam Taer

This Project is developed and designed to function as a Library Management System (LMS). 
We have focused on two main types of book (i.e. textbooks and e-books) for the purpose of the project. Our LMS is a GUI based system. On the platform, users are able to
see the ID of the books that has been added to the library stack, the summary of a book when ID is selected and a section is reserved for the availability of books to borrow.
The system is able to manage the following tasks:

    1. Add any book (textbook or e-book) to library stack

    2. Each book can be registerred by the library manager with the following enteries:
        a. Mandatory - A book ID (unique to only one book regardless of the type of the book)
        b. Mandatory - Title of the book
        c. Mandatory - Author
        d. Mandatory - The year it was published
        e. Mandatory - Edition
        f. Exclusive to ebooks - The book platform where the book can be read from (i.e. OverDrive Read, Fast Read eBook)
        g. Exclusive to ebooks - The genre of the book
        h. Exclusive to textbooks - Cover type of the book (i.e paperback, hardcover case wrap, dust jacket)
        i. Exclusive to textbooks - Book Subject (e.g. math, science, etc)
    
    3. Update book information by library manager - not all info can be updated
        a. Exclusive to ebooks - Platform
        b. Exclusive to ebooks - Genre
        c. Exclusive to textbooks - Cover type
        d. Exclusive to textbooks - Subject of the book

    4. Library manager are able to borrow books from the stack 
    5. Users are able to see the availability status of each book:
        a. The number of books registered
        b. The number of all books borrowed
        c. The number of textbooks and ebooks borrowed
        e. The number of textbooks and ebooks registered
    ** Note: User can also see which specific book is borrowed by looking at its info on our GUI LMS.

    6. Library Manager can delete any books 
    7. Users are able to borrow/return the books that are available (if a user attempt to borrow a book that has already been borrowed, s/he recieves an error message 
    and the same logic applies for attempting to return a book that is not borrowed).
