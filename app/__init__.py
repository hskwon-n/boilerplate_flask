from http import HTTPStatus
from importlib import import_module

from flask import Flask
from werkzeug.exceptions import NotFound

from app.database import db
from app.migrate import migrate


def configure_app(app: Flask, test_config):
    app.config.from_object("config.Config")


def initialize_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True, compare_type=True)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()


def route_app(app: Flask):
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    tuple_module_name = ("user",)

    for module_name in tuple_module_name:
        module = import_module(f"app.{module_name}.route")
        app.register_blueprint(module.blueprint)


def create_app(test_config=None) -> Flask:
    app = Flask(__name__)

    configure_app(app, test_config)

    initialize_extensions(app)

    route_app(app)

    @app.errorhandler(NotFound)
    def not_found_handler(e):
        return "NOT_FOUND", HTTPStatus.NOT_FOUND.value

    return app
