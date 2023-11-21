import os

import pytest
from typer.testing import CliRunner

from PyScoutFM import __version__
from PyScoutFM.application import app

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
    result = runner.invoke(app, ["generate", "--config", "tests/stubs/config.json"])
    assert result.exit_code == 0
    assert os.path.isfile("tests/stubs/outputs/latest.html"), "File was not created"
    clean_up("tests/stubs/outputs/")
