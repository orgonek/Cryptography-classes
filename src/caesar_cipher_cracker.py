from utils import get_random_word
from caesar_cipher import CaesarCipher
import random

class CaesarCracker:
    """ Class used for cracking caesar ciphers using different approaches """

    def __init__(self):
        self.alphabeth_length = 26
        self.cipher = CaesarCipher()

    def generate_data(self):
        shift = random.randint(0,1000)
        word = get_random_word()
        self.cipher.shift = shift
        return self.cipher.encrypt(word)


    def manual_cracking_combinations(self):
        random_word = self.generate_data()
        print(f'----BRUTE FORCE ATTACK----')
        for key in range(self.alphabeth_length):
            self.cipher.shift = key
            print(f'CHECKING KEY #{key} - decrypted text {self.cipher.decrypt(random_word)}')
            print(self.cipher.decrypt(random_word))

