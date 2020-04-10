# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-04-08

from .database import db
from models.ebook import eBook
from models.textbook import Textbook


def drop_tables():
    """Drops entity tables from the 'Book' database"""
    if eBook.table_exists() and Textbook.table_exists():
        db.drop_tables([eBook, Textbook])
