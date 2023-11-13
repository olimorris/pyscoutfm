import typer
from typing_extensions import Annotated

from PyScoutFM.importer import Importer

app = typer.Typer(add_completion=False)


@app.command()
# TODO: Enable users to pass config params via CLI
def main(
    config: Annotated[
        str, typer.Argument(help="The path to the config file to use")
    ] = "config.json"
):
    """
    PyScoutFM

    Use the power of Python to traverse the cosmos and evaluate players within the Football Manager series
    """
    # Load and process the config file
    importer = Importer(config)
    ratings = importer.load_ratings()
    input_file = importer.find_latest_file(importer.config["import_path"], "*.html")

    # Inital data manipulation

    # Compute player ratings

    # Generate the output

    print(f"Hello {config}")


if __name__ == "__main__":
    app()
