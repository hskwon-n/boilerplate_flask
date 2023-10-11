from app.user.repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_list_user(self):
        return self.user_repository.get_list_user()
