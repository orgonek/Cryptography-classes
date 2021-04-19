from string import ascii_letters
import random
import re


class CustomCipher:

    def __init__(self, key: int):
        self.key = key % 30
        self.alphabet = ascii_letters
        self.STARTING_POS = 35
        self.sub_alphabet = self._generate_sub_alphabet()

    def _generate_sub_alphabet(self):
        sub_alphabet = {}
        for letter in self.alphabet:
            ix = ord(letter)
            base = self.key + self.STARTING_POS + ix
            sub_alphabet[letter] = [base, base + 100 + self.key * 7, base + 400 + self.key * 11]

        return sub_alphabet

    def encrypt(self, text):
        with open(text) as file:
            data = file.read()
            data = re.sub("[^a-zA-Z]+", "", data)

        encrypted_text = ''
        for letter in data:
            if letter in self.alphabet:
                number = random.choice(self.sub_alphabet[letter])
                encrypted_text += str(number)
            else:
                encrypted_text += letter

        encrypted_text_save = [encrypted_text[i:i + 90] for i in range(0, len(encrypted_text), 90)]
        print(encrypted_text_save)

        with open('test.txt', 'w+') as file:
            for line in encrypted_text_save:
                file.write(f'{line}\n')

        return encrypted_text
