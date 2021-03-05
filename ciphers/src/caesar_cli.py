import click
from caesar_cipher import CaesarCipher

@click.group()
def cli():
    pass

@click.command()
@click.option('--shift', default=3, help='shift by which each letter should be moved in encryption process')
@click.argument('plaintext', type=str)
def encrypt(plaintext, shift):
    """ Encrypt plaintext using caesar cipher encryption, with specified shift  """
    cipher = CaesarCipher(shift)
    click.echo(cipher.encrypt(plaintext))

@click.command()
@click.argument('encrypted_text', type=str)
@click.option('--shift', default=3, help='shift by which each letter should be moved in decryption process')
def decrypt(encrypted_text, shift):
    """ Decrypt plaintext using caesar cipher decryption, with specified shift  """
    cipher = CaesarCipher(shift)
    click.echo(cipher.decrypt(encrypted_text))

cli.add_command(encrypt)
cli.add_command(decrypt)

if __name__ == '__main__':
    cli()
