import pytest
from manage import seed


@pytest.mark.parametrize(
    "user_id,payload,seeder,expected_status_code",
    [
        # Remove Book from a not owned wishlist
        (4, {"wishlist_id": 1, "book_id": 1}, True, 400),
        # Remove Book from a wishlist with invalid input
        (1, {"wishlist_id": 1}, False, 400),
        # Remove Book from owned wishlist where there is book
        (4, {"wishlist_id": 4, "book_id": 1}, True, 200),
    ],
)
def test_remove_book_from_wishlist(
    flask_app, client, user_id, payload, seeder, expected_status_code
):
    # Given
    seed(flask_app)
    url = f"/wishlist/{user_id}"
    if seeder:
        seed(flask_app)
    response = client.post(url, json=payload)
    # When
    response = client.delete(url, json=payload)
    # Then
    assert response.status_code == expected_status_code


@pytest.mark.parametrize(
    "user_id,payload,seeder,expected_status_code",
    [
        # Add Book to not owned wishlist
        (4, {"wishlist_id": 1, "book_id": 1}, True, 400),
        # Add Book to a wishlist with invalid Input
        (1, {"wishlist_id": 1}, False, 400),
        # Add Book to owned wishlist where there is book
        (4, {"wishlist_id": 4, "book_id": 1}, True, 201),
    ],
)
def test_add_book_to_wishlist(
    flask_app, client, user_id, payload, seeder, expected_status_code
):
    # Given
    url = f"/wishlist/{user_id}"
    if seeder:
        seed(flask_app)
    # When
    response = client.post(url, json=payload)
    # Then
    assert response.status_code == expected_status_code


@pytest.mark.parametrize(
    "user_id,payload,seeder,expected_status_code",
    [
        # Add Books to not owned wishlist
        (4, {"wishlist_id": 1, "book_ids": [1, 2, 3]}, True, 400),
        # Add Books to a wishlist with invalid Input
        (1, {"wishlist_id": 1}, False, 400),
        # Add Books to owned wishlist
        (4, {"wishlist_id": 4, "book_ids": [1,2,3,100]}, True, 200),
    ],
)
def test_add_many_books_to_wishlist(
    flask_app, client, user_id, payload, seeder, expected_status_code
):
    # Given
    url = f"/wishlist/{user_id}"
    if seeder:
        seed(flask_app)
    # When
    response = client.put(url, json=payload)
    # Then
    assert response.status_code == expected_status_code


@pytest.mark.parametrize(
    "user_id,response,seeder,expected_status_code",
    [
        # Get non existing user
        (100, {}, False, 404),
        # Get valid User
        (1, {}, True, 200),
    ],
)
def test_get_user_wishlists(flask_app, client, user_id, seeder, response, expected_status_code):
    # Given
    url = f"/wishlist/{user_id}"
    if seeder:
        seed(flask_app)
    # When
    response = client.get(url)
    # Then
    assert response.status_code == expected_status_code
    if response.status_code == 200:
        assert response.json.get('user', False)
        assert response.json.get('wishlists', False)

@pytest.mark.parametrize(
    "seeder",
    [
        (False,),
        (True,),
    ],
)
def test_get_all(flask_app, client, seeder):
    # Given
    url = f"/wishlist/"
    if seeder:
        seed(flask_app)
    # When
    response = client.get(url)
    assert response.status_code == 200
    if seeder:
        assert response.json[0].get('id', False)
        assert response.json[0].get('name', False)
        assert response.json[0].get('books') == []
    else:
        assert response.json == []
