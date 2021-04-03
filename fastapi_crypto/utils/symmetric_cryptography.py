from cryptography.fernet import Fernet, InvalidToken


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
        status: bool = True

        try:
            value = bytes.fromhex(value)
            f = Fernet(value)
            self.key = value
        except ValueError as e:
            status = False

        return status

    def encode_message(self, message: str):
        """
        Encrypts specified message, using declared key

        Args:
            message: Plain text entered by user

        Returns:
            Encrypted message
        """
        encrypted_message = ''
        try:
            f = Fernet(self.key)
            encrypted_message = f.encrypt(message.encode('UTF-8')).hex()
        except ValueError as e:
            encrypted_message = message

        return encrypted_message

    def decode_message(self, message: str):
        """
        Decrypts given message using stored key

            Args:
                message: Text in hex, provided by user

            Returns:
                Decrypted message
        """
        decrypted_message = "Incorrect value"

        try:
            f = Fernet(self.key)
            decrypted_message = f.decrypt(bytes.fromhex(message))
        except (ValueError, InvalidToken):
            decrypted_message = message

        return decrypted_message
