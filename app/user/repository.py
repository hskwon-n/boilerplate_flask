from typing import Sequence

from app.database import db
from app.models.user_model import UserModel


class UserRepository:
    def get_list_user(self) -> Sequence[UserModel]:
        list_user = db.session.query(UserModel).all()

        return list_user
