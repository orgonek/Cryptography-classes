from string import ascii_letters
import random
import re


class CustomCipher:

    def __init__(self, key: int):
        self.key = key % 30
        self.alphabet = ascii_letters
        self.STARTING_POS = 35
        self.sub_alphabet = self._generate_sub_alphabet()
        self.rev_alphabet = self._generate_reversed_sub_alphabet()

    def _generate_sub_alphabet(self):
        sub_alphabet = {}
        for letter in self.alphabet:
            ix = ord(letter)
            base = self.key + self.STARTING_POS + ix
            sub_alphabet[letter] = [base, base + 100 + self.key * 7, base + 400 + self.key * 11]

        return sub_alphabet

    def _generate_reversed_sub_alphabet(self):
        return {
            value: letter
            for letter, values in self.sub_alphabet.items()
            for value in values
        }

    def encrypt(self, filename):
        with open(filename) as file:
            data = file.read()
            data = re.sub("[^a-zA-Z]+", "", data)

        encrypted_text = ''
        for letter in data:
            if letter in self.alphabet:
                number = random.choice(self.sub_alphabet[letter])
                encrypted_text += str(number)
            else:
                encrypted_text += letter

        encrypted_text_format= [encrypted_text[i:i + 90] for i in range(0, len(encrypted_text), 90)]

        with open(f'encrypted_{filename}', 'w+') as file:
            for line in encrypted_text_format:
                file.write(f'{line}\n')

        return encrypted_text

    def decrypt(self, filename):
        decrypted_text = ''
        with open(filename) as file:
            text = file.read()
            text = re.sub("[^0-9]+", "", text)

        text_formatted = [text[i: i + 3] for i in range(0, len(text), 3)]
        for sign in text_formatted:
            decrypted_text += self.rev_alphabet[int(sign)]

        decrypted_text_format = [decrypted_text[i:i + 90] for i in range(0, len(decrypted_text), 90)]

        with open(f'decrypted_{filename}', 'w+') as file:
            for line in decrypted_text_format:
                file.write(f'{line}\n')
