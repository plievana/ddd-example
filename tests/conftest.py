import os
import pytest

from app import create_app


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    os.environ['MONGO_DB'] = 'testing'
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()