from flask import Flask, jsonify


def route_app(app: Flask):
    @app.route("/hello")
    def hello():
        return "Hello, World!"


def create_app() -> Flask:
    app = Flask(__name__)

    route_app(app)

    return app
