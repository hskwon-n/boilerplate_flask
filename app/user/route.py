from app.user import blueprint
from app.user.controller import UserController
from app.user.repository import UserRepository
from app.user.service import UserService

user_controller = UserController(UserService(UserRepository()))

blueprint.add_url_rule("/", view_func=user_controller.get_list_user)
