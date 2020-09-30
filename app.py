import click
from pathlib import Path


@click.group()
def cli():
    pass


@cli.command()
def init():
    """Creates config file in home directory."""
    cfg_file_path = Path.home().__str__()
    with open(cfg_file_path, mode='w+') as fp:
        pass
