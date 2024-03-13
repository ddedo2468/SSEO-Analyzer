from unittest import TestCase
from app.models import User

class TestUserModel(TestCase):

    def test_user_creation(self):
        """Test if users can be successfully created."""
        user1 = User(user_name="user1", email="user@gmail.com", password='password')
        assert isinstance(user1, User)

if __name__ == '__main__':
    # Run all test cases in this file
    unittest.main()
