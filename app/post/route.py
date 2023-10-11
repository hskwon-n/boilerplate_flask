from app.post import blueprint
from app.post.controller import PostController
from app.post.repository import PostRepository
from app.post.service import PostService

post_controller = PostController(PostService(PostRepository()))

blueprint.add_url_rule("/", view_func=post_controller.increase_count)
