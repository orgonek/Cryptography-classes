import click
from hash_all import HashAll
from utils import create_plot

@click.group()
def cli():
    pass

@click.command()
@click.argument('text', type=str)
def perform_hashing(text):
    """ Hash entered string using available algorithms, and show execution time """
    h = HashAll()
    click.echo(h.perform_hashing(text))


@click.command()
@click.option('--algorithm', default='sha256', help='algorithm that will be used to perform the hashing ')
@click.argument('filepath', type=str)
def perform_file_hashing(filepath, algorithm):
    h = HashAll()
    click.echo(h.perform_file_hashing(filepath, algorithm))


@click.command()
def plot():
    """ Command line interface for plot creation """
    create_plot()

cli.add_command(perform_hashing)
cli.add_command(perform_file_hashing)
cli.add_command(plot)

if __name__ == '__main__':
    cli()