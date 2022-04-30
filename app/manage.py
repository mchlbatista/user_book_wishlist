from flask_migrate import upgrade
from faker import Faker

from models import User, Book, Wishlist

faker = Faker()

USER_COUNT = 5
BOOK_COUNT = 10


def seed(app):
    """
    Seed the DB with data
    """
    with app.app_context():
        for _ in range(USER_COUNT):
            user = User(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                password=faker.sha256(),
            )
            user.save()

            wishlist = Wishlist(user_id=user.id, name=faker.word())
            wishlist.save()

        for _ in range(BOOK_COUNT):
            book = Book(
                title=faker.sentence(),
                author=f"{faker.first_name()} {faker.last_name()}",
                isbn=faker.isbn13(),
                date_publication=faker.date_object(),
            )
            book.save()


def alembic_upgrade(app):
    """Upgrades the database to the latest revision"""
    with app.app_context():
        upgrade()
