import time
from app.post.repository import PostRepository


class PostService:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def increase_count(self, useless_args=None):
        self.post_repository.increase_count()

        time.sleep(1)

        return self.get_count()

    def get_count(self):
        return self.post_repository.get_count()
