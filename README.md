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
    Inspired by the fantastic work of <a href="https://www.youtube.com/@squirrel_plays_fof4318">@squirrel_plays</a> and the contributors on <a href="https://fm-arena.com/thread/1949-fm22-positional-filters-what-are-the-best-attributes-for-each-position/">this</a> thread at <a href="https://fm-arena.com">FM-Arena</a>
</p>

## :sparkles: Features

- Generate scout reports from your squad and scouting screens within FM
- Uses a customisable rating system to score players out of 100
- Tweak or create your own ratings to evaluate players
- Exports the scout report into a pretty HTML file
- Easily search and sort the players in the scout report
- Easily export from the game using the [provided views](extras)

## :zap: Requirements

- Python >= 3.8
- Football Manager (any version that supports the supplied views)
- Windows/MacOS operating systems

## :package: Installation

### Windows

1. Check if you have Python installed by opening up a Command Prompt and typing `python -V`
2. Install [Python](https://www.python.org/downloads/windows/) if you need to
3. Once installed, in the Command Prompt, run:

```sh
pip install pyscoutfm
```

4. Now run `pyscoutfm -V` to verify it's installed

### Mac

1. Check if you have Python installed by opening the Terminal app and typing `python -V`
2. Install [Python](https://docs.python-guide.org/starting/install3/osx/) if you need to
3. Once installed, in the Terminal, run:

```sh
pip install pyscoutfm
```

4. Now run `pyscoutfm -V` to verify it's installed

## :video_game: Getting Started

Firstly, make sure that you have followed the steps in the [Installation](#package-installation) section and then opened up the terminal of your choice. In Windows this will be the Command Prompt and on Mac, the Terminal app.

For the purposes of this section, I'll show you how you can go from zero to generating a scout report.

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

### Generating a Scout Report

By default, the tool comes with a default [config](config.json) file along with some sensible [ratings](ratings.json). We will use those but tweak the `import-path` to match the location from step 5:

6. In your terminal application run the command:

```sh
pyscoutfm generate --import-path=MY_LOCATION
```

Where `MY_LOCATION` is the path from step 5.

> **Note**: The tool is smart enough to only load the most recent _html_ file in the directory you specify

7. Open up `latest.html` in your browser and you should see your players from the squad screen alongside their positional rankings which have been calculated with the tool:

<div align="center">
  <img src="https://github.com/olimorris/PyScoutFM/assets/9512444/01560f9d-2875-4986-b973-caf02aeef3fc" alt="The scout
    report" />
</div>

8. Clicking on the arrows next to the column headings allows you to sort by that column. Also, a helpful search box makes it easier to find specific players.

## :hammer: Advanced usage

To be updated

## :telescope: How does it work?

To be updated
