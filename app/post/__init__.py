from flask import Blueprint


blueprint = Blueprint("post_blueprint", __name__, url_prefix="/posts")
