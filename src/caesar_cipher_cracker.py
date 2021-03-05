from utils import get_random_word, get_random_quote
from caesar_cipher import CaesarCipher
import random

class CaesarCracker:
    """ Class used for cracking caesar ciphers using different approaches """
    def __init__(self):
        self.alphabeth_length = 26
        self.cipher = CaesarCipher()

    def generate_data(self):
        """ Creates and encrypts a word using an external api """

        shift = random.randint(0,1000)
        options = [get_random_word, get_random_quote]
        word = random.choice(options)()
        self.cipher.shift = shift
        return (word.upper(), self.cipher.encrypt(word))

    def manual_cracking_combinations(self):
        """ Uses bruteforce and displays all results """

        random_word = self.generate_data()[1]
        print(f'----BRUTE FORCE ATTACK----')
        for key in range(self.alphabeth_length):
            self.cipher.shift = key
            print(f'CHECKING KEY #{key} - decrypted text {self.cipher.decrypt(random_word)}')
            print(self.cipher.decrypt(random_word))

    def manual_cracking_user(self):
        """ Allows the user to guess shift number """

        answer, word = self.generate_data()
        count = 0
        
        decrypted = False

        while decrypted != True:
            try:
                guess = int(input(f'Try to guess shift number: '))
            except:
                raise(ValueError)

            count += 1

            self.cipher.shift = guess

            if self.cipher.decrypt(word) == answer:
                print(f'You got it right !! answer is {answer}. Number of trials {count}')
                decrypted = True
            else:
                print(f'You missed! Try again')

cipher = CaesarCracker()

cipher.manual_cracking_user()