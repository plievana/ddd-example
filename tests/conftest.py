import os
import pytest

from app import create_app

MONGO_DB = 'testing'


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    os.environ['MONGO_DB'] = MONGO_DB
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    """Cleanup a testing directory once we are finished."""
    def remove_test_database():
        from app import db
        db.get_client().drop_database(MONGO_DB)
    request.addfinalizer(remove_test_database)
