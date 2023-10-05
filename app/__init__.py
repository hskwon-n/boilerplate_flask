from flask import Flask, jsonify


def configure_app(app: Flask):
    app.config.from_object("config.Config")


def route_app(app: Flask):
    @app.route("/hello")
    def hello():
        return "Hello, World!"


def create_app() -> Flask:
    app = Flask(__name__)

    configure_app(app)

    route_app(app)

    return app
