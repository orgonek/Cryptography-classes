from src.caesar_cipher import CaesarCipher

class TestCaesarCipher:

    def test_instance(self):
        cipher = CaesarCipher()
        assert type(cipher) is CaesarCipher
    
    def test_encryption_word(self):
        cipher = CaesarCipher(6)
        assert cipher.encrypt(plaintext="AWESOME") == "GCKYUSK"

    def test_decryption_characters(self):
        cipher = CaesarCipher(80)
        assert cipher.encrypt(plaintext="!@#$%^&*()") == "!@#$%^&*()"

    def test_encryption_sentence(self):
        cipher = CaesarCipher(3)
        assert cipher.encrypt(plaintext="TODAY IS GOING TO BE AN AWESOME DAY FOR YOU.") == "WRGDB LV JRLQJ WR EH DQ DZHVRPH GDB IRU BRX."
    
    def test_large_key(self):
        cipher = CaesarCipher(60)
        assert cipher.encrypt(plaintext="TEST SAMPLE") == "BMAB AIUXTM"

    def test_negative_key(self):
        cipher = CaesarCipher(-10)
        assert cipher.encrypt(plaintext="HAVE FUN") == "XQLU VKD"

    def test_decryption_word(self):
        cipher = CaesarCipher(7)
        assert cipher.decrypt(encrypted_text="WYVNYHTTPUN") == "PROGRAMMING"

    def test_decryption_sentence(self):
        cipher = CaesarCipher(18)
        assert cipher.decrypt(
            encrypted_text="LZW YJWSLWKL YDGJQ AF DANAFY DAWK FGL AF FWNWJ XSDDAFY, TML AF JAKAFY WNWJQ LAEW OW XSDD."
            ) == "THE GREATEST GLORY IN LIVING LIES NOT IN NEVER FALLING, BUT IN RISING EVERY TIME WE FALL."

