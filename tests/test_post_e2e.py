from concurrent.futures import ThreadPoolExecutor
from http import HTTPStatus

from flask.testing import FlaskClient


class TestPostUnit:
    def test_concurrency(self, client: FlaskClient):
        number_of_threads = 100

        with ThreadPoolExecutor(max_workers=number_of_threads) as pool:
            print(
                list(
                    pool.map(client.get, ["/posts/" for _ in range(number_of_threads)])
                )
            )

        response = client.get("/posts/")

        assert response.status_code == HTTPStatus.OK.value
        assert response.get_json().get("count") == number_of_threads + 1
