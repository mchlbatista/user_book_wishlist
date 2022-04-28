from app import db


wishlist_book_table = db.Table(
    "wishlist_book",
    db.Column("wishlist_id", db.Integer, db.ForeignKey("wishlist.id")),
    db.Column("book_id", db.Integer, db.ForeignKey("book.id")),
)
