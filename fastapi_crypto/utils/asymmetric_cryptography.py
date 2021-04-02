from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

from fastapi.openapi.models import Encoding


class Asymmetric:

    def __init__(self):
        self.keys = {}
        self.public_key = None
        self.private_key = None
        self.__generate_random_keys()

    def __generate_random_keys(self, mode: str = 'RSA'):
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
        self.__generate_random_keys()
        return self.keys

    def create_ssh_keys(self):
        self.__generate_random_keys('SSH')
        return self.keys

    def set_keys(self, public_key, private_key):
        self.keys['public'] = public_key
        self.keys['private'] = private_key
        self.public_key = serialization.load_pem_public_key(bytes.fromhex(self.keys['public']))
        self.private_key = serialization.load_pem_private_key(bytes.fromhex(self.keys['private']), password=None)

        return self.keys

    def sign_message(self, message: str):

        return self.private_key.sign(
            message.encode('UTF-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        ).hex()

    def verify_message(self):
        pass

    def encode_message(self, message):
        return self.public_key.encrypt(message.encode('UTF-8'), padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )).hex()

    def decode_message(self, message):
        return self.private_key.decrypt(bytes.fromhex(message), padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        ))


