from pytest_mock import MockerFixture

from app.database import db
from app.models.user_model import UserModel
from app.user.controller import UserController
from app.user.repository import UserRepository
from app.user.service import UserService


class TestUserUnit:
    def test_users(self, mocker: MockerFixture):
        mocker.patch("app.database.db.session.query")
        mocker.patch("app.database.db.session.query.all")
        mocker.patch("app.models.user_model.UserModel")

        user_controller = UserController(UserService(UserRepository()))

        user_controller.get_list_user()

        db.session.query.assert_called_once_with(UserModel)
