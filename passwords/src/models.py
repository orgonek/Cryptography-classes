import os
import hashlib

class Profile:
    """ Contains the essential fields of an account """

    def __init__(self, user : str, password : str) -> None:
        self.user = user
        self.salt = os.urandom(32)
        self.password = self.hash_password(password, self.salt)

    def hash_password(self, password : str, salt : str) -> str:
        """ Creates hashed password using entered text and random salt """
        return hashlib.pbkdf2_hmac('sha256', 
            password.encode('utf-8'),
            salt, 10000
        ).hex()