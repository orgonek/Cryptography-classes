import click
from service import ApplicationService


@click.group()
def cli():
    pass

@cli.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True)
@click.option('--repeat_password', prompt=True, hide_input=True)
def register(username, password, repeat_password):
    if password == repeat_password and app.create_user(username, password):
        click.echo('A user has been created')
        return
    click.echo('You have entered incorrect data, please try again')


@cli.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True)
def login(username, password):
    if app.authenticate_user(username, password):
        click.echo('Authorization successful, you are now logged in')
        return
    click.echo('The information you have provided is incorrect')


if __name__ == "__main__":
    app = ApplicationService()
    cli()