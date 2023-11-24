import os
import shutil
from typing import Optional

import typer
from rich import print
from typing_extensions import Annotated

from pyscoutfm import __version__
from pyscoutfm.data import Data
from pyscoutfm.formatter import Formatter
from pyscoutfm.generator import Generator
from pyscoutfm.importer import Importer

app = typer.Typer(add_completion=False)

# Set the correct paths
local_path = os.path.dirname(os.path.abspath(__file__))
views_path = os.path.abspath(os.path.join(local_path, "extras"))
config_path = os.path.abspath(os.path.join(local_path, "config/config.json"))


@app.command()
def copy_views_to(
    path: Annotated[
        str,
        typer.Option(
            "--path",
            "-p",
            help="The paths to copy the views to",
        ),
    ] = "",
):
    """
    Copy the included views to a specified path before importing into FM
    """
    path = os.path.expanduser(path)

    if not os.path.exists(path):
        return print(f"[bold red]Error:[/bold red] The path '{path}' does not exist")

    for filename in os.listdir(views_path):
        source_file = os.path.join(views_path, filename)

        if os.path.isfile(source_file):
            destination_file = os.path.join(path, filename)

            shutil.copy(source_file, destination_file)
            print(
                f"[bold green]Success:[/bold green] The '{filename}' view has been copied"
            )

    raise typer.Exit()


@app.command()
def generate(
    config_path: str = typer.Option(
        config_path, help="The path to the config file to use"
    ),
    import_path: Optional[str] = typer.Option(
        None, help="The path to the directory to import from"
    ),
    export_path: Optional[str] = typer.Option(
        None, help="The path to the directory to export to"
    ),
    ratings_path: Optional[str] = typer.Option(
        None, help="The path to the ratings file to use"
    ),
    ratings_set: Optional[str] = typer.Option(None, help="The ratings set to use"),
):
    """
    Generate a scouting report from the data exported from FM
    """

    # Load and process the config file
    importer = Importer(config_path)
    c = importer.config

    # Validate the paths
    c["import_path"] = validate_path(import_path, "import") or c["import_path"]
    c["export_path"] = validate_path(export_path, "export") or c["export_path"]
    user_rating = False
    if ratings_path:
        c["ratings_path"] = validate_path(ratings_path, "ratings") or c["ratings_path"]
        user_rating = True

    # Load the ratings and validate the ratings set
    ratings = importer.load_ratings(c["ratings_path"], user_rating)
    if ratings_set and ratings_set not in ratings:
        print(f"The ratings set '{ratings_set}' does not exist")
        raise typer.Exit(1)
    c["ratings_set"] = ratings_set or list(ratings.keys())[0]

    # Processing
    input_file = importer.find_latest_file(c["import_path"], "*.html")
    data = Data(input_file, importer.config)
    data.pre_processing_fixes(ratings)
    process_player_ratings(data, ratings, c["ratings_set"])
    output = data.post_processing_fixes(ratings)

    # Generate output
    html = Formatter(output).to_html()
    Generator.output(html, c["export_path"])
    print(
        f"[bold green]Success:[/bold green] Your scouting report has been generated to '{c['export_path']}'"
    )


def validate_path(path, path_type):
    if path is None:
        return
    expanded_path = os.path.expanduser(path)
    if not os.path.exists(expanded_path):
        print(f"Error: The {path_type} path '{path}' does not exist")
        typer.Exit(1)
    return expanded_path


def process_player_ratings(data, ratings, ratings_set):
    for key, ratings_data in ratings[ratings_set].items():
        data.export[key.upper()] = data.calculator(key, ratings_data)


def version_callback(value: bool):
    if value:
        typer.echo(f"PyScoutFM Version: {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            "-V",
            callback=version_callback,
            help="Show the version and exit.",
        ),
    ] = None,
):
    """
    PyScoutFM

    Use the power of Python to traverse the cosmos and scout for players within the Football Manager game
    """
    pass


if __name__ == "__main__":
    app()
