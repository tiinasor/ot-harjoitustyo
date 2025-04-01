import unittest
from services.user_service import user_service
from repositories.user_repository import user_repository
from models.user import User

class TestUserService(unittest.TestCase):
    def test_creating_new_user_works(self):
        user_service.create_user('user1', 'password1')

        found_user = user_repository.find_user('user1')
        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.username, 'user1')
