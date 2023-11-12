import typer
from typing_extensions import Annotated

app = typer.Typer(add_completion=False)


def validate(config):
    return True


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
    if validate(config):
        typer.echo("Validated")

    # Validate the config file

    # Load the config file

    # Begin computing the player ratings

    # Generate the output

    print(f"Hello {config}")


if __name__ == "__main__":
    app()
