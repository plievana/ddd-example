import os
import pytest

from flask import Flask
from app import create_app
from app.hexagonal.shared.infrastructure.mongo_connection import MongoDB

MONGO_DB = 'testing'


def remove_test_database(mongo_client: MongoDB):
    mongo_client.client.drop_database(MONGO_DB)


def get_mongo_client(app: Flask) -> MongoDB:
    return MongoDB(app.config['MONGO_HOST'], app.config['MONGO_PORT'], app.config['MONGO_DB'],
                   app.config.get('MONGO_USER'), app.config.get('MONGO_PASS'))


@pytest.fixture(scope="session")
def app(request):
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    os.environ['MONGO_DB'] = MONGO_DB
    app = create_app()

    mongo_client = get_mongo_client(app)

    request.addfinalizer(lambda: remove_test_database(mongo_client))

    yield app


@pytest.fixture(scope="class")
def mongo_client(request, app):
    request.cls.mongo_client = get_mongo_client(app)


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
