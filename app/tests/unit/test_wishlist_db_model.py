import pytest
from manage import seed
from models import Wishlist


def test_add_book(flask_app):
    # Given
    seed(flask_app)
    with flask_app.app_context():
        # When
        wishlist = Wishlist.add_book(user_id=1, wishlist_id=1, book_id=1)
        # Then
        assert wishlist.id == 1
        assert wishlist.name
        assert len(wishlist.books) == 1
        assert wishlist.books[0].id == 1


@pytest.mark.parametrize(
    "user_id,wishlist_id,book_ids,expected_wishlist",
    [
        # Valid user, wishlist and book (Except one book. It should be ignored)
        (1, 1, [1, 2, 3, 100], True),
        # Invalid wishlist user relationship
        (1, 4, [1, 2], False),
    ],
)
def test_add_many_books(flask_app, user_id, wishlist_id, book_ids, expected_wishlist):
    # Given
    seed(flask_app)
    with flask_app.app_context():
        # When
        wishlist = Wishlist.add_many_books(
            user_id=user_id, wishlist_id=wishlist_id, book_ids=book_ids
        )
        if expected_wishlist:
            # Then
            assert wishlist.id == 1
            assert wishlist.name
            assert len(wishlist.books) == 3
            for book_id in range(3):
                assert wishlist.books[book_id].id == book_id + 1


@pytest.mark.parametrize(
    "user_id,wishlist_id,book_id,expected_wishlist",
    [
        # Valid user, wishlist and book
        (1, 1, 1, True),
        # Invalid wishlist user relationship
        (1, 4, 1, False),
        # Invalid Book
        (1, 1, 2, False),
    ],
)
def test_remove_book(flask_app, user_id, wishlist_id, book_id, expected_wishlist):
    # Given
    seed(flask_app)
    with flask_app.app_context():
        # When
        # Add a book
        wishlist = Wishlist.add_book(user_id=1, wishlist_id=1, book_id=1)
        wishlist = Wishlist.remove_book(
            user_id=user_id, wishlist_id=wishlist_id, book_id=book_id
        )
        # Then
        if expected_wishlist:
            assert wishlist.id == 1
            assert wishlist.name
            assert len(wishlist.books) == 0
        else:
            assert wishlist is None
