from string import ascii_uppercase


class CaesarCipher:
    """ A class used for encryption and decryption,
    using Caesar Cipher  """

    def __init__(self, shift : int = 3):
        self.shift = shift
        self.alphabet = ascii_uppercase
        self.alphabet_length = len(self.alphabet)

    def encrypt(self, plaintext : str) -> str:
        """ Encrypts given text using Caesar Cipher """

        encrypted_text = ""

        for letter in plaintext.upper():
            if letter in self.alphabet:
                new_letter = (self.alphabet.index(letter) + self.shift) % self.alphabet_length
                encrypted_text += self.alphabet[new_letter]
            else :
                encrypted_text += letter
        
        return encrypted_text

    
    def decrypt(self, encrypted_text : str) -> str:
        """ Decrypts given text using Caesar Cipher """

        plaintext = ""

        for letter in encrypted_text.upper():
            if letter in self.alphabet:
                new_letter = (self.alphabet.index(letter) - self.shift) % self.alphabet_length
                plaintext += self.alphabet[new_letter]
            else:
                plaintext += letter

        return plaintext


class VigenereCipher:
    """ A class used for encryption and decryption,
    using Vigenere Cipher  """

    def __init__(self, key : str = "vigenere"):
        self.key = key
        self.alphabet = ascii_uppercase
        self.alphabet_length = len(self.alphabet)
        self.key_length = len(self.key)

    def encrypt(self, plaintext : str) -> str:
        """ Encrypts the plaintext using the specified key """

        plaintext = [letter for letter in plaintext.upper() if letter in self.alphabet]
        plaintext = ''.join(plaintext)

        repeated_key = self.generate_repeated_key(plaintext, self.key.upper())

        return (
            ''.join(self.alphabet[(self.alphabet.index(letter) + self.alphabet.index(repeated_key[i])) % self.alphabet_length]
                for i, letter in enumerate(plaintext))
        )

    def decrypt(self, encrypted_text : str) -> str:
        """ Decrypts the cipher using the specified key """
        
        encrypted_text = [letter for letter in encrypted_text.upper() if letter in self.alphabet]
        encrypted_text = ''.join(encrypted_text)

        repeated_key = self.generate_repeated_key(encrypted_text, self.key.upper())

        return (
            ''.join(self.alphabet[(self.alphabet.index(letter) - self.alphabet.index(repeated_key[i])) % self.alphabet_length]
                for i, letter in enumerate(encrypted_text))
        )

    def generate_repeated_key(self, string : str, key : str) -> str:
        """ Converts key to text length """
        return key if len(string) == len(key) else ''.join(key[i % len(key)]
            for i in range(len(string))
    )

