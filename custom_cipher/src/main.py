from cipher import CustomCipher

custom_cipher = CustomCipher(2)
encrypted_text = custom_cipher.encrypt('sample.txt')
custom_cipher.save_to_file(encrypted_text, 'encrypted.txt')
decrypted_file = custom_cipher.decrypt('file_encrypted.txt')
custom_cipher = custom_cipher.save_to_file(decrypted_file, 'Solved.txt')


