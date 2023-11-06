import re

from setuptools import setup


def get_version():
    with open("src/PyScoutFM/__init__.py", "r", encoding="utf-8") as init_file:
        contents = init_file.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", contents, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="PyScoutFm",
    version=get_version(),
    packages=["PyScoutFM"],
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "pyscoutfm=PyScoutFM.application:main",  # Adjust this line as per your package structure
        ],
    },
    description="Python scouting tool for the Football Manager game",
    url="https://github.com/olimorris/pyscoutfm",
    author="Oli Morris",
    author_email="olimorris@users.noreply.github.com",
    license="MIT",
    install_requires=["click>=8.1.7"],
    classifiers=[],
)
