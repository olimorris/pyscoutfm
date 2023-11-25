<p align="center">
    <img src="https://github.com/olimorris/PyScoutFM/assets/9512444/c79dfc9b-efdc-4b23-bd1d-d485a2f715f0" height="300">
</p>

<h1 align="center">PyScoutFM</h1>

<p align="center">
<a href="https://github.com/olimorris/PyScoutFM/stargazers"><img src="https://img.shields.io/github/stars/olimorris/PyScoutFM?color=c678dd&logoColor=e06c75&style=for-the-badge"></a>
<a href="https://github.com/olimorris/PyScoutFM/issues"><img src="https://img.shields.io/github/issues/olimorris/PyScoutFM?color=%23d19a66&style=for-the-badge"></a>
<a href="https://github.com/olimorris/PyScoutFM/blob/main/LICENSE"><img src="https://img.shields.io/github/license/olimorris/PyScoutFM?color=%2361afef&style=for-the-badge"></a>
<a href="https://github.com/olimorris/PyScoutFM/actions/workflows/ci-cd.yml"><img src="https://img.shields.io/github/actions/workflow/status/olimorris/PyScoutFM/ci-cd.yml?branch=main&label=tests&style=for-the-badge"></a>
</p>

<p align="center">
    Use the power of Python to traverse the cosmos and scout for players within the <a href="https://www.footballmanager.com">Football Manager</a> game<br><br>Inspired by the fantastic work of <a href="https://www.youtube.com/@squirrel_plays_fof4318">@squirrel_plays</a> and the contributors on <a href="https://fm-arena.com/thread/1949-fm22-positional-filters-what-are-the-best-attributes-for-each-position/">this</a> thread at <a href="https://fm-arena.com">FM-Arena</a>
</p>

## :sparkles: Features

- :mag: Generate scout reports from your squad and scouting screens within FM
- :bar_chart: Uses a customisable rating system to score players out of 100
- :wrench: Tweak or create your own weightings to evaluate players
- :file_folder: Exports the scout report into a pretty HTML file
- :mag_right: Easily search and sort the players in the scout report
- :rocket: Easily export from the game using the [provided views](src/pyscoutfm/extras)

## :zap: Requirements

- Python >= 3.10
- Football Manager (any version that supports the supplied views)
- Windows/MacOS

## :package: Installation

1. Check if you have Python installed by opening up a Command Prompt/Terminal and typing `python -V`
2. Install [Python](https://www.python.org/downloads/) if you don't.

> **Note**: If you're on Windows, follow [this guide](WINDOWS_INSTALL.md) and if you're on Mac, I suggest using [Homebrew](https://brew.sh)

3. Once installed, in the Command Prompt/Terminal, run:

```
pip install pyscoutfm
```

4. To verify the installation, run:

```
pyscoutfm -v
```

## :video_game: Generating a Scout Report

Let's get down to business and show you how quickly you can generate a scouting report for your current squad from the command line.

1. Firstly, and for reference, to see a list of the commands and options available to you at any step of the way with PyScoutFM, append `--help` to a [command](#rocket-commands):

```
pyscoutfm generate --help
```

### Export data from FM

The tool requires an extract of data from Football Manager. To make this easy, we can use the _views_ that come supplied with PyScoutFM.

2. To save you hunting for them, run:

```
pyscoutfm copy-views-to --path="MY_LOCATION"
```

> Where `MY_LOCATION` is the path you wish to copy the views to

3. Import these views into FM; we'll start with the main squad screen of the team you're managing but note that you could go into your scouting screen as well:

<div align="center">
  <img src="https://github.com/olimorris/PyScoutFM/assets/9512444/bf1a1711-6d40-4c93-b77f-06a8aba216dc" alt="importing a view" />
</div>

4. In the squad screen, use <kbd>Ctrl</kbd>+<kbd>a</kbd> (Windows) or <kbd>⌘</kbd>+<kbd>a</kbd> (Mac) to select all of the players in the screen (this can be laggy!), followed by <kbd>Ctrl</kbd>+<kbd>p</kbd>/<kbd>⌘</kbd>+<kbd>p</kbd>, selecting _Web Page_ as the print format:

<div align="center">
  <img src="https://github.com/olimorris/PyScoutFM/assets/9512444/1d7c7254-1a41-4aed-ad01-3e825ba0e78b" alt="printing a screen" />
</div>

5. Save the printed file into your chosen location:

<div align="center">
  <img src="https://github.com/olimorris/PyScoutFM/assets/9512444/87282629-35b7-4fad-a5e0-360eef3d12a3" alt="saving the print file" />
</div>

### Generating the Scout Report

By default, the tool comes with a default [config](src/pyscoutfm/config/config.json) file along with some sensible [attribute weightings](src/pyscoutfm/config/weightings.json). We will use those but tweak the `import-path` option to match the location from step 5:

6. In your terminal application run the command:

```
pyscoutfm generate --import-path=MY_LOCATION --export-path=MY_LOCATION
```

Where `MY_LOCATION` is the path from step 5.

> **Note**: The tool is smart enough to only load the most recent _html_ file in the directory you specify

7. You should see a _Success_ message confirming the generation of the report.

### Using the Scout Report

So you have a Scout Report, now what?

8. Open up `latest.html` in your browser and you should see your players from the squad screen alongside their positional ratings which have been calculated with the tool:

<div align="center">
  <img src="https://github.com/olimorris/PyScoutFM/assets/9512444/d6e1c53c-dfbd-4645-9314-04590d09ef71" alt="The scout
    report" />
</div>

9. Clicking on the arrows next to the column headings allows you to sort by that column. Also, a helpful search box makes it easier to find specific players.

10. Each of the rating columns represents a score out of 100. That is, how well suited a player is to a particular position based on the attribute weightings defined in the default [weightings file](src/pyscoutfm/config/weightings.json)

### Hints and Tips

You may find yourself tweaking your search results in Football Manager and re-generating scouting reports often. Below are some tips for doing this optimally:

1. Always export your Football Manager data to the same location. The tool is smart enough to be able to load the most recent HTML file in a directory if you don't pass it an `import_path` parameter.

2. You don't need to re-type your command in the Command Prompt/Terminal. Instead use the <kbd>Up</kbd> key to scroll through historical commands.

3. Once the report has been generated, just refresh the webpage in the Browser. The tool will always overwrite the `latest.html`. Don't worry though...it also saves a datetime stamped copy of the report as well.

## :rocket: Commands

To get started, run:

    pyscoutfm --help

The available options are:

    Usage: pyscoutfm [OPTIONS] COMMAND [ARGS]...

    Options:
    --version  -V        Show the version and exit.
    --help               Show this message and exit.

    Commands:
    copy-views-to       Copy the included views to a specified path before importing into FM
    generate            Generate a scouting report from the data exported from FM

### Copy Views Command

    Usage: pyscoutfm copy-views-to [OPTIONS]

    Copy the included views to a specified path before importing into FM

    Options:
    --path  -p      TEXT  The paths to copy the views to
    --help                Show this message and exit.

### Generate Command

    Usage: pyscoutfm generate [OPTIONS]

    Generate a scouting report from the data exported from FM

    Options:
    --config-path         TEXT  The path to the config file to use
    --import-path         TEXT  The path to the directory to import from [default: None]
    --export-path         TEXT  The path to the directory to export to [default: None]
    --weightings-path     TEXT  The path to the weightings file to use [default: None]
    --weightings-set      TEXT  The weightings set to use [default: None]
    --help                      Show this message and exit.

## :hammer: Advanced usage

To be updated

## :telescope: How does it work?

To be updated
