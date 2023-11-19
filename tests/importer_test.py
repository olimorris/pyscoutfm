import json
import os
import time
from unittest.mock import mock_open, patch

import pytest

from PyScoutFM.importer import Importer


@pytest.fixture
def sample_config():
    return {"ratings_path": "~/ratings.json"}


@pytest.fixture
def sample_ratings():
    return {"rating1": 4.5, "rating2": 3.7}


def test_load_config_from_file(sample_config):
    with patch(
        "builtins.open", mock_open(read_data=json.dumps(sample_config))
    ) as mock_file:
        importer = Importer("dummy_config_path.json")
        mock_file.assert_called_once_with("dummy_config_path.json", "r")
        assert importer.config == sample_config


def test_get_last_file():
    importer = Importer("tests/stubs/config.json")
    test_path = os.getcwd() + "/tests/stubs/inputs"
    file_path = test_path + "/Squad.html"

    # Update the modification time of Squad.html to make it the latest file
    current_time = time.time()
    os.utime(file_path, (current_time, current_time))

    assert importer.find_latest_file(test_path, "*.html") == test_path + "/Squad.html"
