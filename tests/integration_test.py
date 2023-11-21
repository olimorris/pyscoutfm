import pytest
from typer.testing import CliRunner

from PyScoutFM import __version__
from PyScoutFM.application import app

runner = CliRunner()


def test_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert f"PyScoutFM Version: {__version__}" in result.stdout
