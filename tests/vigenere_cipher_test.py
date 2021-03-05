from src.vigenere_cipher import VigenereCipher

class TestCaesarCipher:

    def test_instance(self):
        cipher = VigenereCipher()
        assert type(cipher) is VigenereCipher

    def test_encryption_word(self):
        cipher = VigenereCipher(key="university")
        assert cipher.encrypt(plaintext="Just playing around") == "DHAOTCSGBLANZJYEV"

    def test_special_characters(self):
        cipher = VigenereCipher(key="test")
        assert cipher.encrypt(plaintext="THIS#IS@GENERAL@PROBLEM!@$%^") == "MLALBWYXGIJTETJHUPWF"

    def test_long_key(self):
        cipher = VigenereCipher("INCREDIBLE")
        assert cipher.encrypt("sample") == "ANOGPH"

    def test_decryption_word(self):
        cipher = VigenereCipher("hype")
        assert cipher.decrypt("WPDKYYBQPLV") == "PROGRAMMING"

    def test_key_generator(self):
        cipher = VigenereCipher()
        cipher.generate_repeated_key(string="ABCDE", key="CDE") == "CEGFHJ"
