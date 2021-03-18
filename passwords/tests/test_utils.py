from src.utils import hash_password
import os

class TestUtils:
    """ Class for testing utils functionality """
    
    def test_password_hashing(self):
        password = "123456"
        assert password != hash_password(password, os.urandom(32))


