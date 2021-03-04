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
