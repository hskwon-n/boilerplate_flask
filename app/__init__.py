from http import HTTPStatus

from flask import Flask
from werkzeug.exceptions import NotFound


def configure_app(app: Flask, test_config):
    if test_config is None:
        app.config.from_object("config.Config")
    else:
        app.config.from_mapping(test_config)


def route_app(app: Flask):
    @app.route("/hello")
    def hello():
        return "Hello, World!"


def create_app(test_config=None) -> Flask:
    app = Flask(__name__)

    configure_app(app, test_config)

    route_app(app)

    @app.errorhandler(NotFound)
    def not_found_handler(e):
        return "NOT_FOUND", HTTPStatus.NOT_FOUND.value

    return app
