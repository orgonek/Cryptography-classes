from cryptography.fernet import Fernet


class Symmetric:
    """
    Stores methods related to symmetric cryptography
    """

    def __init__(self):
        self.key = ""

    def create_key(self):
        """
           Generates random symmetric key
        """
        self.key = Fernet.generate_key()
        return self.key.hex()

    def set_key(self, value: str):
        """
            Allows user to change key value

            Args:
                value: Key specified by user (hex)

        """
        self.key = bytes.fromhex(value)

    def encode_message(self, message: str):
        """
        Encrypts specified message, using declared key

        Args:
            message: Plain text entered by user

        Returns:
            Encrypted message
        """
        f = Fernet(self.key)
        return f.encrypt(message.encode('UTF-8')).hex()

    def decode_message(self, message: str):
        """
        Decrypts given message using stored key

            Args:
                message: Text in hex, provided by user

            Returns:
                Decrypted message
        """
        f = Fernet(self.key)
        return f.decrypt(bytes.fromhex(message))
