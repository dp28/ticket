import click


@click.group()
def cli():
    pass


@cli.command()
def run():
    click.echo('Hello, ticket')


if __name__ == '__main__':
    cli()
