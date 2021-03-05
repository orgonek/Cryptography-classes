import click
from caesar_cipher_cracker import CaesarCracker

@click.group()
def cli():
    pass

@click.command()
def manual_combinations():
    """ Uses bruteforce to display all options"""
    cracker = CaesarCracker()
    cracker.manual_cracking_combinations()

@click.command()
def manual_user_cracking():
    """ Allows user to guess shift"""
    cracker = CaesarCracker()
    cracker.manual_cracking_user()

@click.command()
@click.argument('encrypted_text', type=str, default='default')

def automatic_cracker(encrypted_text):
    """ Automatic cracking using bruteforce and english dictionary"""
    cracker = CaesarCracker()
    click.echo(f"Status {cracker.automatic_cracking(encrypted_text)}")

cli.add_command(manual_combinations)
cli.add_command(manual_user_cracking)
cli.add_command(automatic_cracker)

if __name__ == '__main__':
    cli()
