from steganography import Steganography
from ciphers import CaesarCipher, VigenereCipher
import click

s = Steganography()
c = CaesarCipher()
v = VigenereCipher()

@click.group()
def cli():
    click.echo('Enter a file name you want to process (with ext)')

@cli.command()
@click.option('--path', prompt=True, help='Enter a path, where your image is located')
@click.option('--message', prompt=True)
def encode_message(path, message):
    choice = input('Do you want to encrypt text ? (y/n)')
    if choice.lower() == 'y':
        cipher = input('Which cipher do you want to use Caesar or Vigenere (c/v)')
        if cipher.lower() == 'c':
            message = c.encrypt(message)
        elif cipher.lower() =='v':
            message = v.encrypt(message)

    name = input('Enter a file name of a new image: ')
    Steganography.encode(path, message, name)

@cli.command()
@click.option('--path', prompt=True, help='Enter a path, where your image is located')
def decode_message(path):
    message = Steganography.decode(path)
    print(message)

    choice = input('Did you use cipher to encrypt text ? (y/n)')
    if choice.lower() == 'y':
        cipher = input('Which cipher was used to encrypt message (c/v)')
        if cipher.lower() == 'c':
            message = c.decrypt(message)
            print(message)
        elif cipher.lower() =='v':
            message = v.decrypt(message)
            print(message)

    click.echo(f'Decrypted message:{ message }')

        





if __name__ == '__main__':
    cli()