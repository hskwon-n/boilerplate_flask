from app.user import blueprint
from app.user.controller import UserController

user_controller = UserController()

blueprint.add_url_rule("/", view_func=user_controller.get_list_user)
