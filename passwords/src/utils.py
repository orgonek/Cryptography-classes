import hashlib


def hash_password(password : str, salt : str) -> str:
    """ Creates hashed password using entered text and random salt """
    return hashlib.pbkdf2_hmac(
            hash_name='sha256', 
            password=password.encode('utf-8'),
            salt=salt, 
            iterations=10000
        ).hex()