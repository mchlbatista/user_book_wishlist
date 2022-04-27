import pytest
from flask_migrate import upgrade, downgrade
from main import app


@pytest.fixture()
def flask_app():

    with app.app_context():
        upgrade()

    yield app

    with app.app_context():
        downgrade()


@pytest.fixture()
def client(flask_app):
    return flask_app.test_client()
