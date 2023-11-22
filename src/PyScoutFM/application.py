import os
import shutil
from typing import Optional

import typer
from rich import print
from typing_extensions import Annotated

from PyScoutFM import __version__
from PyScoutFM.data import Data
from PyScoutFM.formatter import Formatter
from PyScoutFM.generator import Generator
from PyScoutFM.importer import Importer

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
    config: Annotated[
        str, typer.Option(help="The path to the config file to use")
    ] = config_path,
    import_path: Annotated[
        Optional[str], typer.Option(help="The path to the directory to import from")
    ] = None,
    export_path: Annotated[
        Optional[str], typer.Option(help="The path to the directory to export to")
    ] = None,
    ratings_path: Annotated[
        Optional[str], typer.Option(help="The path to the ratings file to use")
    ] = None,
):
    """
    Generate a scouting report from the data exported from FM
    """

    # Load and process the config file
    importer = Importer(config)
    c = importer.config

    # Validate the import path
    # TODO: Refactor this mes
    if import_path is not None:
        import_path = os.path.expanduser(import_path)
        if not os.path.exists(import_path):
            return print(
                f"[bold red]Error:[/bold red] The path '{import_path}' does not exist"
            )

        c["import_path"] = import_path

    # Validate the export path
    if export_path is not None:
        export_path = os.path.expanduser(export_path)
        if not os.path.exists(export_path):
            return print(
                f"[bold red]Error:[/bold red] The path '{export_path}' does not exist"
            )

        c["export_path"] = export_path

    # Validate the ratings_path
    if ratings_path is not None:
        ratings_path = os.path.expanduser(ratings_path)
        if not os.path.exists(ratings_path):
            return print(
                f"[bold red]Error:[/bold red] The path '{ratings_path}' does not exist"
            )

        c["ratings_path"] = ratings_path

    ratings = importer.load_ratings(ratings_path)
    input_file = importer.find_latest_file(c["import_path"], "*.html")

    # Fix the input data
    data = Data(input_file, importer.config)
    data.pre_processing_fixes(ratings)

    # Compute player ratings
    for key, ratings_data in ratings[c["ratings_set"]].items():
        data.export[key.upper()] = data.calculator(key, ratings_data)

    # Fix the output data
    output = data.post_processing_fixes(ratings)

    # Generate the output
    html = Formatter(output).to_html()
    Generator.output(html, c["export_path"])

    print(
        f"[bold green]Success:[/bold green] Your scouting report has been generated to '{c['export_path']}'"
    )


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
