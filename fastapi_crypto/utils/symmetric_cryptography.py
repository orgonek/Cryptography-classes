from cryptography.fernet import Fernet


class Symmetric:

    def __init__(self):
        self.key = ""

    def create_key(self):
        self.key = Fernet.generate_key()
        return self.key.hex()

    def set_key(self, value: str):
        self.key = bytes.fromhex(value)

    def encode_message(self, message: str):
        f = Fernet(self.key)
        return f.encrypt(message.encode('UTF-8')).hex()

    def decode_message(self, message: str):
        f = Fernet(self.key)
        return f.decrypt(bytes.fromhex(message))

