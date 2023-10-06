from http import HTTPStatus

from flask.testing import FlaskClient


def test_users(client: FlaskClient):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK.value
