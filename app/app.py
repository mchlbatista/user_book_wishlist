from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from logging.config import dictConfig

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)

db = SQLAlchemy()
api = Api(version="0.1", title="Book Wishlist", description="Zonar Systems")


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    db.init_app(app)
    api.init_app(app)

    # Migrations Manager
    migrate = Migrate(app, db)
    from models import User, Book, Wishlist, wishlist_book_table

    # Resources
    from views.wishlist_resource import UserWishlistResource, WishlistResource

    return app
