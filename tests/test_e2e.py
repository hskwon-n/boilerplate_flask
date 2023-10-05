from http import HTTPStatus

from flask.testing import FlaskClient


def test_hello(client: FlaskClient):
    response = client.get("/hello")

    assert response.status_code == HTTPStatus.OK.value


def test_not_found(client: FlaskClient):
    response = client.get("/not_found")

    assert response.status_code == HTTPStatus.NOT_FOUND.value
