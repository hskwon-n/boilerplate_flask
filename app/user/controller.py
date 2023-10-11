from typing import Sequence

from app.models.user_model import UserModel
from app.user.service import UserService


class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get_list_user(self):
        list_user: Sequence[UserModel] = self.user_service.get_list_user()

        return [{"id": user.id} for user in list_user]
