from http import HTTPStatus

from flask import jsonify

from app.post.service import PostService


class PostController:
    def __init__(self, post_service: PostService):
        self.post_service = post_service

    def increase_count(self):
        self.post_service.increase_count()

        count = self.post_service.get_count()

        return jsonify({"count": count}), HTTPStatus.OK.value
