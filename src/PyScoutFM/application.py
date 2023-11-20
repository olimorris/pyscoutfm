from typing import Optional

import typer
from typing_extensions import Annotated

from PyScoutFM import __version__
from PyScoutFM.data import Data
from PyScoutFM.formatter import Formatter
from PyScoutFM.generator import Generator
from PyScoutFM.importer import Importer

app = typer.Typer(add_completion=False)


def version_callback(value: bool):
    if value:
        print(f"PyScoutFM {__version__}")
        raise typer.Exit()


@app.command()
# TODO: Enable users to pass config params via CLI
def main(
    config: Annotated[
        str, typer.Argument(help="The path to the config file to use")
    ] = "config.json",
    version: Annotated[
        Optional[bool],
        typer.Option("--version", "-V", callback=version_callback, is_eager=True),
    ] = None,
):
    """
    PyScoutFM

    Use the power of Python to traverse the cosmos and scout players within the Football Manager series
    """

    # Load and process the config file
    importer = Importer(config)
    ratings = importer.load_ratings()
    c = importer.config
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


if __name__ == "__main__":
    app()
