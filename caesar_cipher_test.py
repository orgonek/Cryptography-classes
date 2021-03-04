from caesar_cipher import CaesarCipher

class TestCaesarCipher:
    
    def test_encryption(self):
        cipher = CaesarCipher(6)
        sample_plaintext = "Coronavirus statistics in Poland"
        assert cipher.encrypt(sample_plaintext) == "IUXUTGBOXAY YZGZOYZOIY OT VURGTJ" 
        
        cipher.shift = 50
        sample_plaintext = "samplemail@gmail.com"
        assert cipher.encrypt(sample_plaintext) == "QYKNJCKYGJ@EKYGJ.AMK" 

    def test_decryption(self):
        cipher = CaesarCipher(3)
        encrypted_text = "WRGDB LV JRLQJ WR EH DQ DZHVRPH GDB IRU BRX."
        assert cipher.decrypt(encrypted_text) == "TODAY IS GOING TO BE AN AWESOME DAY FOR YOU."
        
        cipher.shift = 26
        encrypted_text = "JUST FOR FUN"
        assert cipher.decrypt(encrypted_text) == "JUST FOR FUN"
        

