import numpy as np
from PIL import Image

DELIMITER = '$be4l'

class Steganography:

    @staticmethod
    def encode(src, message, dest):
        """
            Encoding the message inside image
        """        
        
        img = Image.open(src, 'r')
        width, height = img.size

        array = np.array(list(img.getdata()))

        if img.mode == 'RGB':
            n = 3
        elif img.mode == 'RGBA':
            n = 4

        total_pixels = array.size // n
        message += DELIMITER

        binary_message = ''.join([format(ord(i), '08b') for i in message])
        message_len = len(binary_message)

        if message_len > total_pixels:
            print('Error')
        
        else:
            index = 0
            for i in range(total_pixels):
                for j in range(0, 3):
                    if index < message_len:
                        array[i][j] = int(bin(array[i][j])[2:9] + binary_message[index], 2)
                        index += 1

            array = array.reshape(height, width, n)
            encoded_image = Image.fromarray(array.astype('uint8'), img.mode)
            encoded_image.save(dest)

            print('Image encoded')

        

    @staticmethod
    def decode(src):
        """
            Decoding the message from image
        """        
        
        img = Image.open(src, 'r')
        array = np.array(list(img.getdata()))

        if img.mode == 'RGB':
            n = 3
        elif img.mode == 'RGBA':
            n = 4
        
        total_pixels = array.size // n
        
        hidden_bits = ""

        for i in range(total_pixels):
            for j in range(0, 3):
                hidden_bits += (bin(array[i][j])[2:][-1])

        hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

        message = ""

        for i in range(len(hidden_bits)):
            if message[-5:] == DELIMITER:
                break
            else:
                message += chr(int(hidden_bits[i], 2))

        if DELIMITER in message:
            print("Hidden message", message[:-5])
        else:
            print("No hidden message")


