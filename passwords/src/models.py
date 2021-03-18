import os
from utils import hash_password

class Account:
    """ Contains the essential fields of an account """

    def __init__(self, name : str = "Elon", password : str = "User") -> None:
        self._name = name
        self._salt = os.urandom(32)
        self._password = hash_password(password, self._salt)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value : str):
        self._name = value
    
    @property
    def salt(self):
        return self._salt

    @salt.setter
    def salt(self, value = os.urandom(32)):
        self._salt = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = hash_password(new_password, self._salt)