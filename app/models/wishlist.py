from sqlalchemy.sql import func
from app import db

from . import Book
from models.wishlist_book import wishlist_book_table


class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    name = db.Column(db.String(255))
    created_at = db.Column(
        db.DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    books = db.relationship(
        "Book", secondary=wishlist_book_table, backref="wishlists", lazy="joined"
    )

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def add_book(user_id, wishlist_id, book_id):
        """
        Validate input and add Book to a given Wishlist
        """
        # Validate that the given Wishlist belongs to the given User
        wishlist = Wishlist.query.filter_by(id=wishlist_id, user_id=user_id).first()
        book = Book.query.get(book_id)

        # Validate Wishlist & Book
        if all([wishlist, book]):
            wishlist.books.append(book)
            db.session.commit()
            return wishlist

    @staticmethod
    def add_many_books(user_id, wishlist_id, book_ids):
        """
        Validate input and add Books to a given Wishlist
        """
        # Validate that the given Wishlist belongs to the given User
        wishlist = Wishlist.query.filter_by(id=wishlist_id, user_id=user_id).first()
        books = Book.query.filter(Book.id.in_(book_ids))

        # Validate Wishlist & Book
        if all([wishlist, books]):
            wishlist.books.extend(books)
            db.session.commit()
            return wishlist

    @staticmethod
    def remove_book(user_id, wishlist_id, book_id):
        """
        Validate input and remove Book from a given Wishlist
        """
        # Validate that the given Wishlist belongs to the given User
        wishlist = Wishlist.query.filter_by(id=wishlist_id, user_id=user_id).first()
        book = Book.query.get(book_id)

        # Validate that the Wishlist and Book exists and the Book is part of the Wishlist
        if all([wishlist, book]) and book in wishlist.books:
            wishlist.books.remove(book)
            db.session.commit()
            return wishlist
