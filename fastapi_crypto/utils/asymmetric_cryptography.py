from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding, utils

from fastapi.openapi.models import Encoding


class Asymmetric:
    """
    Stores asymmetric functions
    """

    def __init__(self):
        self.keys = {}
        self.public_key = None
        self.private_key = None
        self.__generate_random_keys()

    def __generate_random_keys(self, mode: str = 'RSA'):
        """
        Generates and assigns public and private key, depending on the option selected (RSA/ SSH)
        Args:
            mode: name of format style
        """
        options = {'encoding': serialization.Encoding.PEM,
                   'format': serialization.PrivateFormat.TraditionalOpenSSL,
                   'encryption_algorithm': serialization.NoEncryption(),
                   'public_encoding': serialization.Encoding.PEM,
                   'format_public': serialization.PublicFormat.SubjectPublicKeyInfo,
                   }

        if mode == 'SSH':
            options['format'] = serialization.PrivateFormat.OpenSSH
            options['public_encoding'] = serialization.Encoding.OpenSSH
            options['format_public'] = serialization.PublicFormat.OpenSSH

        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )

        self.public_key = self.private_key.public_key()

        self.keys['private'] = self.private_key.private_bytes(
            encoding=options['encoding'],
            format=options['format'],
            encryption_algorithm=options['encryption_algorithm'],
        ).hex()

        self.keys['public'] = self.private_key.public_key().public_bytes(
            encoding=options['public_encoding'],
            format=options['format_public']
        ).hex()

    def create_keys(self):
        """
        Creates public and private keys, using PEM encoding
        """
        self.__generate_random_keys()
        return self.keys

    def create_ssh_keys(self):
        """
        Creates public and private keys, using SSH encoding
        """
        self.__generate_random_keys('SSH')
        return self.keys

    def set_keys(self, public_key, private_key):
        """
        Allows user to set public and private key
        Args:
            public_key: Public key specified by user (hex)
            private_key: Private key specified by user (hex)

        """
        self.keys['public'] = public_key
        self.keys['private'] = private_key
        self.public_key = serialization.load_pem_public_key(bytes.fromhex(self.keys['public']))
        self.private_key = serialization.load_pem_private_key(bytes.fromhex(self.keys['private']), password=None)

        return self.keys

    def sign_message(self, message: str):
        """
        Signs message given by user
        Args:
            message: Plain text, entered by user

        Returns:
            signature: hex based string, which allows user to verify message
        """
        return self.private_key.sign(
            message.encode('UTF-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        ).hex()

    def verify_message(self, message, signature):
        """
        Checks if private key associated with public key was used to sign specific message
        Args:
            message: Message to check
            signature: Signed signature

        """
        return self.public_key.verify(
            bytes.fromhex(signature),
            message.encode('UTF-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

    def encode_message(self, message):
        """
        Encrypts message using public key
        Args:
            message: Plain text entered by user

        Returns: Encrypted message

        """
        return self.public_key.encrypt(message.encode('UTF-8'), padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )).hex()

    def decode_message(self, message):
        """
        Decrypts message using private key
        Args:
            message: Hex value entered by user

        Returns: Decrypted message

        """
        return self.private_key.decrypt(bytes.fromhex(message), padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        ))
