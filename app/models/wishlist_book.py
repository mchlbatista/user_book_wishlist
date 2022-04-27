from app import db


# class WishlistBook(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     wishlist_id = db.Column(db.Integer, db.ForeignKey("wishlist.id"))
#     book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
#     created_at = db.Column(
#         db.DateTime(timezone=True), server_default=func.now(), nullable=False
#     )

#     def save(self):
#         db.session.add(self)
#         db.session.commit()


wishlist_book_table = db.Table(
    "wishlist_book",
    db.Column("wishlist_id", db.Integer, db.ForeignKey("wishlist.id")),
    db.Column("book_id", db.Integer, db.ForeignKey("book.id")),
)
