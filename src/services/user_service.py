from models.user import User
from repositories.user_repository import user_repository

class UserService:
    def __init__(
        self,
        user_repository=user_repository
    ):
        self._user_repository = user_repository

    def create_user(self, username, password):
        user = self._user_repository.create(User(username, password))

        return user

user_service = UserService()
