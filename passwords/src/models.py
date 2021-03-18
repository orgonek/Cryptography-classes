import os
import hashlib

class Account:
    """ Contains the essential fields of an account """

    def __init__(self, name : str, password : str) -> None:
        self.name = name
        self.salt = os.urandom(32)
        self.password = self.hash_password(password, self.salt)

    def hash_password(self, password : str, salt : str) -> str:
        """ Creates hashed password using entered text and random salt """
        return hashlib.pbkdf2_hmac(
            hash_name='sha256', 
            password=password.encode('utf-8'),
            salt=salt, 
            iterations=10000
        ).hex()