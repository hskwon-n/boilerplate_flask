import pytest
from app import create_app
from flask import Flask


@pytest.fixture()
def app():
    app = create_app(
        {
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture()
def client(app: Flask):
    return app.test_client()
