import glob
import importlib.resources as pkg_resources
import json
import os
from typing import Any, Dict, Optional

package_name = "pyscoutfm"
config_directory = "config"


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

    def load_ratings(self, ratings_path, user_rating):
        """
        Load ratings data from a file specified in the config.
        """
        # If the user doesn't specify a ratings path, use the default.
        if not user_rating:
            ratings_path = self.config.get("ratings_path")

            # Construct the path to the resource
            resource_path = (
                pkg_resources.files(f"{package_name}.{config_directory}") / ratings_path
            )

        else:
            resource_path = os.path.expanduser(ratings_path)

        try:
            with open(resource_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Could not find {ratings_path} in the {package_name}.{config_directory} package."
            )

    def find_latest_file(self, path: str, extension: str) -> Optional[str]:
        """
        Find the latest file in a given directory with a specific extension.
        """
        files = glob.glob(os.path.join(os.path.expanduser(path)) + "/" + extension)
        files.sort(key=os.path.getmtime)

        return files[-1] if files else None
