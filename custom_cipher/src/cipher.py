from string import ascii_letters
import random
import re


class CustomCipher:
    """
    This class contains custom cipher implementation
    """

    def __init__(self, key: int):
        self.key = key % 30
        self.alphabet = ascii_letters
        self.STARTING_POS = 35
        self.sub_alphabet = self._generate_sub_alphabet()
        self.rev_alphabet = self._generate_reversed_sub_alphabet()

    def _generate_sub_alphabet(self) -> dict:
        """
        Generates substitution alphabet for each letter
        Returns: dictionary with key value pairs

        """
        sub_alphabet = {}
        for letter in self.alphabet:
            ix = ord(letter)
            base = self.key + self.STARTING_POS + ix
            sub_alphabet[letter] = [base, base + 100 + self.key * 7, base + 400 + self.key * 11]

        return sub_alphabet

    def _generate_reversed_sub_alphabet(self) -> dict:
        """
        Generates reversed substitution alphabet for decrypting cipher
        Returns: dictionary where key is number and value is letter

        """
        return {
            value: letter
            for letter, values in self.sub_alphabet.items()
            for value in values
        }

    @staticmethod
    def _reverse_row(row: str):
        """
        Args:
            row: line of cipher

        Returns: reversed line of cipher

        """
        return row[::-1]

    def _process_data(self, text: str):
        """
        Process data based on position in text

        """
        text_formatted = [text[i:i + 90] for i in range(0, len(text), 90)]

        result = ''
        for i, line in enumerate(text_formatted):
            if i % 5 == 0:
                half = len(line) // 2
                result += self._reverse_row(line[:half])
                result += line[half:]
            elif i % 2 == 0 and i % 4 != 0:
                result += self._reverse_row(line)
            else:
                result += line

        return result

    def encrypt(self, filename) -> str:
        """
        Encrypts file with custom cipher
        Args:
            filename: name of file to encrypt

        Returns: encrypted text

        """
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

        encrypted_text = self._process_data(encrypted_text)

        return encrypted_text

    def decrypt(self, filename):
        """
        Decrypts custom cipher included in file
        Args:
            filename: name of file which should be decrypted

        Returns: Decrypted text
        """
        decrypted_text = ''
        with open(filename) as file:
            text = file.read()
            text = re.sub("[^0-9]+", "", text)

        decrypted_text = self._process_data(text)

        text_formatted = [decrypted_text[i: i + 3] for i in range(0, len(decrypted_text), 3)]
        decrypted_text = ''
        for sign in text_formatted:
            decrypted_text += self.rev_alphabet[int(sign)]

        return decrypted_text

    @staticmethod
    def save_to_file(text: str, filename: str):
        """
        Saves text to file, 90 characters per line
        Args:
            text: text to be saved
            filename: name of file
        """
        text_formatted = [text[i:i + 90] for i in range(0, len(text), 90)]

        with open(f'file_{filename}', 'w+') as file:
            for line in text_formatted:
                file.write(f'{line}\n')
