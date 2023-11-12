import typer

app = typer.Typer()


@app.command()
def main(config: str):
    print(f"Hello {config}")


if __name__ == "__main__":
    app()
