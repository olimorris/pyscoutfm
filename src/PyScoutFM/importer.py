import glob
import json
import os
from typing import Any, Dict, Optional


class Importer:
    """
    Load the config data and subsequent files.
    """

    def __init__(self, config_path: str):
        self.config = self.load_config_from_file(config_path)

    def load_config_from_file(self, config_path: str) -> Dict[str, Any]:
        """
        Load and parse a JSON config file.
        """
        with open(os.path.expanduser(config_path), "r") as file:
            return json.load(file)

    def load_ratings(self) -> Any:
        """
        Load ratings data from a file specified in the config.
        """
        ratings_path = self.config.get("ratings_path")
        if ratings_path:
            with open(os.path.expanduser(ratings_path), "r") as file:
                return json.load(file)
        else:
            raise ValueError("Ratings path not found in the configuration.")

    def find_latest_file(self, path: str, extension: str) -> Optional[str]:
        """
        Find the latest file in a given directory with a specific extension.
        """
        files = glob.glob(os.path.join(os.path.expanduser(path), extension))
        if files:
            return max(files, key=os.path.getctime)
        return None
