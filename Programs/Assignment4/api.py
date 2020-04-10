# Group 16
# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-04-08


from models.ebook import eBook
from database.database import db
from models.textbook import Textbook
from database.create_tables import create_tables
from database.drop_tables import drop_tables
from models.library_manager import LibraryManager
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

# I have tried importing the 'create_tables' & 'drop_tables'
# They didn't work, but i kept the py files :)
db.drop_tables([eBook, Textbook])
db.create_tables([eBook, Textbook])

# create_tables()
# drop_tables()

library = LibraryManager(name="Maryam")
book1 = Textbook(book_id='A111', book_title='why do we need to sleep?', author='John Simpliciano',
                 published_year=2017, edition=3, cover_type='hardcover case wrap', book_subject='health')
book2 = Textbook(book_id='B222', book_title='color methology', author='Maryam Taer', published_year=2002,
                 edition=4, cover_type='paperback', book_subject='arts')
book3 = Textbook(book_id='V654', book_title='Hamlet', author='Shakespeare', published_year=2000,
                 edition=10, cover_type='hardcover dust jacket', book_subject='literature')
book4 = Textbook(book_id='F009', book_title='Mein Kampf', author='Adolf Hitler', published_year=1925,
                 edition=6, cover_type='paperback', book_subject='history')
book5 = eBook(book_id='B20V2', book_title='Me', author='Elton John', published_year=2017,
              edition=4, platform='OverDrive Read', book_genre='biography')
book6 = eBook(book_id='M3K12', book_title='Pax', author='Sara Pennypacker', published_year=2012,
              edition=5, platform='OverDrive Read', book_genre='kids')
book7 = eBook(book_id='L091A', book_title='Deadpool Vol.4: Monkey Business', author='Daniel Way',
              published_year=2019, edition=5, platform='Fast Read ebooks', book_genre='comics')

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)
library.add_book(book7)


@app.route("/library_manager/<book_type>", methods=["POST"])
def add_book(book_type):
    data = request.json
    try:
        if book_type == "textbook":
            textbook = Textbook(book_id=data["book_id"], book_title=data["title"], author=data["author"],
                                published_year=data["published_year"], edition=data["edition"],
                                cover_type=data["cover_type"], book_subject=data["subject"])
            library.add_book(textbook)

        elif book_type == "ebook":
            ebook = eBook(book_id=data["book_id"], book_title=data["title"], author=data["author"],
                          published_year=data["published_year"], edition=data["edition"],
                          platform=data["platform"], book_genre=data["genre"])
            library.add_book(ebook)

        else:
            return make_response(f'Invalid book_type "{book_type}"!', 400)

    except (KeyError, ValueError) as error:
        message = str(error)
        return make_response(message, 400)
    else:
        return make_response(data["book_id"], 200)


@app.route("/library_manager/<book_type>/<book_id>", methods=["PUT"])
def update_book(book_id, book_type):
    data = request.json
    book = library.get_book_by_id(book_id)

    if not book:
        return make_response(f"{book_type} not found.", 404)
    try:
        if book_type == "textbook":
            if "subject" not in data.keys():
                return make_response("Invalid JSON: missing subject", 404)
            if "cover_type" not in data.keys():
                return make_response("Invalid JSON: missing cover type", 404)
            library.update_book(book_id, data["subject"], data["cover_type"])

        elif book_type == "ebook":
            if "platform" not in data.keys():
                return make_response("Invalid JSON: missing platform", 404)
            if "genre" not in data.keys():
                return make_response("Invalid JSON: missing genre", 404)
            library.update_book(book_id, data["platform"], data["genre"])
        else:
            return make_response(f'Invalid book_type "{book_type}"!', 400)

    except ValueError as error:
        message = str(error)
        return make_response(message, 400)
    else:
        return make_response("", 200)


@app.route("/library_manager/<book_id>/borrow", methods=["PUT"])
def borrow_book(book_id):
    """ Tries to quarantine someone in school """
    try:
        library.get_book_by_id(book_id).borrow(book_id)
        return make_response(f"{book_id} is now in quarantine.", 200)
    except ValueError:
        return make_response(f"{book_id} is not in school.", 400)


@app.route("/library_manager/<book_id>/return_book", methods=["PUT"])
def return_book(book_id):
    """ Tries to release someone in school from quarantine"""
    try:
        library.get_book_by_id(book_id).return_book(book_id)
        return make_response(f"{book_id} is now in released.", 200)
    except ValueError:
        return make_response(f"{book_id} is not in school.", 400)


@app.route("/library_manager/book/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = library.get_book_by_id(book_id)
    if not book:
        return make_response("Book not found.", 404)
    try:
        library.remove_book(book_id)
    except KeyError as error:
        message = str(error)
        return make_response(message, 400)
    else:
        return make_response("", 200)


@app.route("/library_manager/all", methods=["GET"])
def list_books():
    return make_response(jsonify(library.to_dict()), 200)


@app.route("/library_manager/book/<book_id>", methods=["GET"])
def get_book_by_id(book_id):
    book = library.get_book_by_id(book_id)

    if not book:
        return make_response("Book not found.", 404)
    return make_response(jsonify(library.get_book_by_id(book_id).to_dict()), 200)


@app.route("/library_manager/all/<book_type>", methods=["GET"])
def get_book_by_type(book_type):
    book = library.get_books_by_type(book_type)
    if not book:
        return make_response("Book not found.", 404)

    return make_response(jsonify(library.get_books_by_type(book_type)), 200)


@app.route("/library_manager/all/stats", methods=["GET"])
def get_book_stats():
    return make_response(jsonify(library.get_book_stat().to_dict()), 200)


@app.route("/validate", methods=["GET", "POST", "PUT", "DELETE"])
def validate_setup():
    return jsonify(
        {
            "method": request.method,
            "Content-Type header": request.headers.get("Content-Type"),
            "data": request.data.decode(),
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
