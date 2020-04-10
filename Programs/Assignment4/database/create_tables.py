# Group 16
# Maryam Taer & John Simpliciano
# Set 2C
# 2020-04-08


from .database import db
from models.ebook import eBook
from models.textbook import Textbook


def create_tables():
    """Creates entity tables in the 'Book' database"""
    db.create_tables([eBook, Textbook])

