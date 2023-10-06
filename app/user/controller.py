from app.database import db
from app.models.user_model import UserModel


class UserController:
    def get_list_user(self):
        list_user = db.session.query(UserModel).all()

        return [{"id": user.id} for user in list_user]
