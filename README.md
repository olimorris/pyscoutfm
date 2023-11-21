<p align="center">
    <img src="https://github.com/olimorris/PyScoutFM/assets/9512444/c79dfc9b-efdc-4b23-bd1d-d485a2f715f0" height="300">
</p>

<h1 align="center">PyScoutFM</h1>

<p align="center">
<a href="https://github.com/olimorris/pyscoutfm/stargazers"><img src="https://img.shields.io/github/stars/olimorris/pyscoutfm?color=c678dd&logoColor=e06c75&style=for-the-badge"></a>
<a href="https://github.com/olimorris/pyscoutfm/issues"><img src="https://img.shields.io/github/issues/olimorris/pyscoutfm?color=%23d19a66&style=for-the-badge"></a>
<a href="https://github.com/olimorris/pyscoutfm/blob/main/LICENSE"><img src="https://img.shields.io/github/license/olimorris/pyscoutfm?color=%2361afef&style=for-the-badge"></a>
<a href="https://github.com/olimorris/pyscoutfm/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/olimorris/pyscoutfm/test.yml?branch=main&label=tests&style=for-the-badge"></a>
</p>

<p align="center">
    Use the power of Python to traverse the cosmos and scout for players within the <a href="https://www.footballmanager.com">Football Manager</a> game<br><br>
    Inspired by the fantastic work of <a href="https://www.youtube.com/@squirrel_plays_fof4318">@squirrel_plays</a> and the contributors on this thread at <a href="https://fm-arena.com/thread/1949-fm22-positional-filters-what-are-the-best-attributes-for-each-position/">FM-Arena</a>
</p>

## :sparkles: Features

- Uses a customisable rating system to score players out of 100
- Tweak or create your own ratings to evaluate players
- Export the computed data into a pretty HTML file
- Easily search and sort the players in the export
- Easily export from the game using the [provided views](extras)

## :zap: Requirements

- Python >= 3.6
- Football Manager (any version that supports the supplied views)
- Windows/MacOS operating systems

## :package: Installation

### Windows

1. Install [Python](https://www.python.org/downloads/windows/)
2. Verify it's installed by opening up a Command Prompt and running `python -V`
3. Then in the Command Prompt, run `pip install pyscoutfm`
4. Now run `pyscoutfm -V` to verify it's installed

### Mac

1. Install Python - [This guide](https://docs.python-guide.org/starting/install3/osx/) is a great resource
2. Verify it's installed by opening the Terminal app and running `python -V`
3. Then in the Terminal, run `pip install pyscoutfm`
4. Now run `pyscoutfm -V` to verify it's installed

## :video_game: Getting Started

Firstly, make sure that you have followed the steps in the [Installation](#package-installation) section and then opened up the terminal of your choice. In Windows this will be the Command Prompt and on Mac, the Terminal app.

For the purposes of this section, I'll show you how you can go from zero to having a rated list of players from FM.

1. Firstly, and for reference, to see a list of the commands and options available to you at any step of the way with PyScoutFM, append `--help` to a command. For example:

```sh
pyscoutfm --help
```

But let's focus on getting some player data out of FM. To do this, we'll need to use the _views_ that come supplied with PyScoutFM.

### Export data from FM

2. Run:

```sh
pyscoutfm copy-views-to --path="MY_LOCATION"
```

> Where `MY_LOCATION` is the path you wish to copy the views to

3. Import these views into FM; we'll start with the main squad screen of the team you're managing:

<div align="center">
  <img src="https://github.com/olimorris/PyScoutFM/assets/9512444/bf1a1711-6d40-4c93-b77f-06a8aba216dc" alt="importing a view" />
</div>

4. In the squad screen, use <kbd>Ctrl</kbd>+<kbd>a</kbd> (Windows) or <kbd>⌘</kbd>+<kbd>a</kbd> (Mac) to select all of the players in the screen, followed by <kbd>Ctrl</kbd>+<kbd>p</kbd>/<kbd>⌘</kbd>+<kbd>p</kbd>, selecting _Web Page_ as the print format:

<div align="center">
  <img src="https://github.com/olimorris/PyScoutFM/assets/9512444/1d7c7254-1a41-4aed-ad01-3e825ba0e78b" alt="printing a screen" />
</div>

5. Save the printed file into your chosen location:

<div align="center">
  <img src="https://github.com/olimorris/PyScoutFM/assets/9512444/87282629-35b7-4fad-a5e0-360eef3d12a3" alt="saving the print file" />
</div>

### Rank players with PyScoutFM

By default, the tool comes with a preset [config](config.json) file along with some sensible [ratings](ratings.json). We will use those but tweak the `import_path` to match the location from step 5:

6. In your terminal application run the command:

```sh
pyscoutfm generate --import_path=MY_LOCATION
```

Where `MY_LOCATION` is the path from step 5.

> **Note**: The tool is smart enough to only load the most recent _html_ file in the directory you specify

7. Open up `latest.html` in your browser and you should see your players from the squad screen alongside their positional rankings which have been calculated with the tool:

<div align="center">
  <img src="https://github.com/olimorris/PyScoutFM/assets/9512444/0f7697a1-8ccc-4225-8c43-ac70cbdc55e7" alt="Output from the tool" />
</div>

8. Clicking on the arrows next to the column headings allows you to sort by that column. Also, a helpful search box makes it easier to find specific players.

