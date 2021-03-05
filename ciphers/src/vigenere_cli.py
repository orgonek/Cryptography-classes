import click
from vigenere_cipher import VigenereCipher

@click.group()
def cli():
    pass

@click.command()
@click.option('--key', default="vigenere", help='Key from which a new string will be created ')
@click.argument('plaintext', type=str)
def encrypt(plaintext, key):
    """ Encrypt plaintext using vigenere cipher encryption, with specified key  """
    cipher = VigenereCipher(key)
    click.echo(cipher.encrypt(plaintext))

@click.command()
@click.argument('encrypted_text', type=str)
@click.option('--key', default="vigenere", help='Key by which each letter will be moved in decryption process')
def decrypt(encrypted_text, key):
    """ Decrypt plaintext using vigenere cipher decryption, with specified key  """
    cipher = VigenereCipher(key)
    click.echo(cipher.decrypt(encrypted_text))

cli.add_command(encrypt)
cli.add_command(decrypt)

if __name__ == '__main__':
    cli()
