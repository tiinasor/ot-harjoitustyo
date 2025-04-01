from models.user import User
from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, user):
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO Users (username, password) VALUES (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        return user
    
    def find_user(self, username):
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM Users WHERE username = ?",
            (username,)
        )

        row = cursor.fetchone()

        return User(row["username"], "") if row else None

user_repository = UserRepository(get_database_connection())
