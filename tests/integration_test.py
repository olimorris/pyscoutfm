import os

import pytest
from typer.testing import CliRunner

from pyscoutfm import __version__
from pyscoutfm.application import app

runner = CliRunner()

@pytest.fixture
def clean_up_output_dir():
    output_dir = "tests/stubs/outputs/"
    yield
    for item in os.listdir(output_dir):
        item_path = os.path.join(output_dir, item)
        if os.path.isfile(item_path):
            os.remove(item_path)

def test_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert f"PyScoutFM Version: {__version__}" in result.stdout

def test_generate(clean_up_output_dir):
    result = runner.invoke(
        app, ["generate", "--config-path", "tests/stubs/config.json"]
    )
    assert result.exit_code == 0
    assert os.path.isfile("tests/stubs/outputs/latest.html"), "File was not created"

def test_generate_custom_weightings(clean_up_output_dir):
    result = runner.invoke(
        app,
        [
            "generate",
            "--config-path",
            "tests/stubs/config.json",
            "--weightings-path",
            "tests/stubs/custom_weightings.json",
            "--weightings-set",
            "olis_weightings",
        ],
    )
    assert result.exit_code == 0
    assert os.path.isfile("tests/stubs/outputs/latest.html"), "File was not created"

def test_wrong_rating_set_fails(clean_up_output_dir):
    result = runner.invoke(
        app,
        [
            "generate",
            "--config-path",
            "tests/stubs/config.json",
            "--weightings-path",
            "tests/stubs/custom_weightings.json",
            "--weightings-set",
            "ykykyk_balanced",  # This set does not exist within the custom weightings file
        ],
    )
    assert result.exit_code == 1
    assert not os.path.isfile(
        "tests/stubs/outputs/latest.html"
    ), "File was created when it should not have been"
