from .PgnSplitter import PgnSplitter
import os
import click

@click.command()
@click.argument('filepath')
def main(filepath):
    """
    Creates the PGN files
    """
    if not os.path.isfile(filepath):
        click.echo("Please give a file that exists")
    elif ".pgn" not in filepath:
        click.echo("Please provide the filepath to a PGN")
    else:
        click.echo(f"Splitting the file {filepath}")
        ps = PgnSplitter(filepath=filepath)
        counter, dirpath = ps.execute()
        click.echo(f"{counter} files created in the folder {dirpath}")

