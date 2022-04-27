from app import api
from flask_restx import fields


wishlist_book_model = api.model(
    "Add Book",
    {
        "wishlist_id": fields.Integer(required=True, min=1, description="Wishlist ID"),
        "book_id": fields.Integer(required=True, min=1, description="Book ID"),
    },
)

wishlist_many_books_models = api.model(
    "Add Books",
    {
        "wishlist_id": fields.Integer(required=True, min=1, description="Wishlist ID"),
        "book_ids": fields.List(fields.Integer, required=True)
    }
)

user = api.model(
    "User",
    {
        "id": fields.Integer,
        "first_name": fields.String,
        "last_name": fields.String,
        "email": fields.String,
    },
)

book = api.model(
    "Wishlist book entry",
    {
        "id": fields.Integer,
        "title": fields.String,
        "author": fields.String,
        "isbn": fields.String,
        "date_publication": fields.String,
    },
)

wishlist_model = api.model(
    "Wishlist",
    {
        "id": fields.Integer,
        "name": fields.String,
        "books": fields.List(fields.Nested(book)),
    },
)

user_wishlist_model = api.model(
    "User Wishlist",
    {
        "user": fields.Nested(user),
        "wishlists": fields.List(fields.Nested(wishlist_model)),
    },
)
