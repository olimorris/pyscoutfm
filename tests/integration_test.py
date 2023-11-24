import os

import pytest
from typer.testing import CliRunner

from pyscoutfm import __version__
from pyscoutfm.application import app

runner = CliRunner()


def clean_up(dir):
    for item in os.listdir(dir):
        item_path = os.path.join(dir, item)
        if os.path.isfile(item_path):
            os.remove(item_path)


def test_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert f"PyScoutFM Version: {__version__}" in result.stdout


def test_generate():
    result = runner.invoke(
        app, ["generate", "--config-path", "tests/stubs/config.json"]
    )
    assert result.exit_code == 0
    assert os.path.isfile("tests/stubs/outputs/latest.html"), "File was not created"
    clean_up("tests/stubs/outputs/")


def test_generate_custom_ratings():
    result = runner.invoke(
        app,
        [
            "generate",
            "--config-path",
            "tests/stubs/config.json",
            "--ratings-path",
            "tests/stubs/custom_ratings.json",
            "--ratings-set",
            "olis_ratings",
        ],
    )
    assert result.exit_code == 0
    assert os.path.isfile("tests/stubs/outputs/latest.html"), "File was not created"
    clean_up("tests/stubs/outputs/")


def test_wrong_rating_set_fails():
    result = runner.invoke(
        app,
        [
            "generate",
            "--config-path",
            "tests/stubs/config.json",
            "--ratings-path",
            "tests/stubs/custom_ratings.json",
            "--ratings-set",
            "ykykyk_balanced",  # This set does not exist within the custom ratings file
        ],
    )
    assert result.exit_code == 1
    assert not os.path.isfile(
        "tests/stubs/outputs/latest.html"
    ), "File was created when it should not have been"
    clean_up("tests/stubs/outputs/")
