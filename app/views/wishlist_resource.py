from flask import request
from flask_restx import Resource
from models import Wishlist, User
from .api_models.wishlist import (
    wishlist_book_model,
    wishlist_many_books_models,
    user_wishlist_model,
    wishlist_model,
)
from app import api
from sqlalchemy.orm import joinedload


wishlist_ns = api.namespace("wishlist", description="User Book Wishlist operations")


@wishlist_ns.route("/")
class WishlistResource(Resource):
    """
    Wishlist Operations
    """

    @wishlist_ns.marshal_with(wishlist_model, as_list=True)
    def get(self):
        """
        List all wishlist in the DB
        """
        return Wishlist.query.all(), 200


@wishlist_ns.route("/<int:user_id>")
class UserWishlistResource(Resource):
    """
    User specific Wishlist Operations
    """

    @wishlist_ns.marshal_with(user_wishlist_model)
    def get(self, user_id):
        """
        Get all Wishlists for the given user
        """
        user = (
            User.query.options(joinedload(User.wishlists)).filter_by(id=user_id).first()
        )
        if user:
            wishlist_formatted = [
                {"id": w.id, "name": w.name, "books": w.books} for w in user.wishlists
            ]
            return {"user": user, "wishlists": wishlist_formatted}, 200
        api.abort(404, "User does not exists")

    @wishlist_ns.expect(wishlist_book_model, validate=True)
    @wishlist_ns.marshal_with(wishlist_model)
    @api.doc(
        responses={
            201: "New book added to wishlist added.",
            400: "Invalid User, Book or Wishlist IDs.",
        }
    )
    def post(self, user_id):
        """
        Add new Book to an existent Wishlist
        """
        body = request.get_json()
        wishlist = Wishlist.add_book(user_id, body["wishlist_id"], body["book_id"])
        if wishlist:
            return wishlist, 201
        api.abort(400, "Invalid User, Book or Wishlist IDs.")

    @wishlist_ns.expect(wishlist_many_books_models, validate=True)
    @wishlist_ns.marshal_with(wishlist_model)
    @api.doc(
        responses={
            200: "All valid books added to wishlist.",
            400: "Invalid User or Wishlist IDs.",
        }
    )
    def put(self, user_id):
        """
        Add many book to a wishlist
        """
        body = request.get_json()

        wishlist = Wishlist.add_many_books(user_id, body["wishlist_id"], body["book_ids"])
        if wishlist:
            return wishlist, 200
        api.abort(400, "Invalid User, Books or Wishlist IDs.")

    @wishlist_ns.expect(wishlist_book_model, validate=True)
    @wishlist_ns.marshal_with(wishlist_model)
    @api.doc(
        responses={
            200: "Book removed from wishlist.",
            400: "Invalid User, Book or Wishlist IDs.",
        }
    )
    def delete(self, user_id):
        """
        Remove a Book from an existent Wishlist
        """
        body = request.get_json()

        wishlist = Wishlist.remove_book(user_id, body["wishlist_id"], body["book_id"])
        if wishlist:
            return wishlist, 200
        api.abort(400, "Invalid User, Book or Wishlist IDs.")
