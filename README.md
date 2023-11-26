<p align="center">
    <img src="https://github.com/olimorris/PyScoutFM/assets/9512444/c79dfc9b-efdc-4b23-bd1d-d485a2f715f0">
</p>

<h1 align="center">PyScoutFM</h1>

<p align="center">
<a href="https://github.com/olimorris/PyScoutFM/stargazers"><img src="https://img.shields.io/github/stars/olimorris/PyScoutFM?color=c678dd&logoColor=e06c75&style=for-the-badge"></a>
<a href="https://github.com/olimorris/PyScoutFM/issues"><img src="https://img.shields.io/github/issues/olimorris/PyScoutFM?color=%23d19a66&style=for-the-badge"></a>
<a href="https://github.com/olimorris/PyScoutFM/blob/main/LICENSE"><img src="https://img.shields.io/github/license/olimorris/PyScoutFM?color=%2361afef&style=for-the-badge"></a>
<a href="https://github.com/olimorris/PyScoutFM/actions/workflows/test.yml"><img src="https://img.shields.io/github/actions/workflow/status/olimorris/PyScoutFM/test.yml?branch=main&label=tests&style=for-the-badge"></a>
</p>

<p align="center">
    Use the power of Python to traverse the cosmos and scout for players within the <a href="https://www.footballmanager.com">Football Manager</a> game<br><br>Inspired by the fantastic work of <a href="https://www.youtube.com/@squirrel_plays_fof4318">@squirrel_plays</a> and the contributors on <a href="https://fm-arena.com/thread/1949-fm22-positional-filters-what-are-the-best-attributes-for-each-position/">this</a> thread at <a href="https://fm-arena.com">FM-Arena</a>
</p>

## ✨ Features

- 🔍 Generate scout reports from your squad and scouting screens within FM
- 📊 Uses a customisable rating system to score players out of 100
- 🔧 Tweak or create your own weightings to evaluate players
- 📂 Exports the scout report into a pretty HTML file
- 🔭 Easily search and sort the players in the scout report
- 🚀 Easily export from the game using the [provided views](src/pyscoutfm/extras)

## ⚡ Requirements

- Python >= 3.10
- Football Manager (any version that supports the supplied views)
- Windows/MacOS

## 📦 Installation

### Cloud (easiest)

1. On this page, click `Code` > `Create codespace on main`:

<img src="https://github.com/olimorris/PyScoutFM/assets/9512444/22df9106-3c27-409a-93f5-d09bc23979ca">

2. Click on `Bash` in the terminal of the next window that opens:

<img src="https://github.com/olimorris/PyScoutFM/assets/9512444/e50548bc-975e-4988-88c1-8541f1641b22">

3. Then run `pip install -e .`

<img src="https://github.com/olimorris/PyScoutFM/assets/9512444/46511647-95c3-46ef-a874-c14f5ac874e1">

4. Now running `pyscoutfm -V` will output the current version of the tool indicating the install was successful!

### Locally (more convenient)

1. Check if you have Python installed by opening up a Command Prompt/Terminal and typing `python -V`
2. Install [Python](https://www.python.org/downloads/) if you don't.

> **Note**: If you're on Windows, follow [this guide](WINDOWS_INSTALL.md) and if you're on Mac, I suggest using [Homebrew](https://brew.sh)

3. Once installed, in the Command Prompt/Terminal, run:

```
pip install pyscoutfm
```

4. To verify the installation, run:

```
pyscoutfm -V
```

## 🎮 Generating a Scout Report

Let's get down to business and show you how quickly you can generate a scouting report for your current squad from the command line.

1. Firstly, and for reference, to see a list of the commands and options available to you at any step of the way with PyScoutFM, append `--help` to a [command](#rocket-commands):

```
pyscoutfm generate --help
```

### Export data from FM

The tool requires an extract of data from Football Manager. To make this easy, we can use the _views_ that come supplied with PyScoutFM.

2. To save you hunting for them, run:

Cloud:
```
pyscoutfm copy-views-to
```

or Local:
```
pyscoutfm copy-views-to --path="MY_LOCATION"
```

> Where `MY_LOCATION` is the path you wish to copy the views to

3. Download the views (if on Cloud and as per this [screenshot](https://github.com/olimorris/PyScoutFM/assets/9512444/676239cd-ed7b-4ce7-af27-f049a57ab578)) then import them into FM; we'll start with the main squad screen of the team you're managing but note that you could go into your scouting screen as well:

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

6. _(Optional)_ If you're using the Cloud install, make sure you upload the exported HTML file to the Codespace:

<div align="center">
    <img src="https://github.com/olimorris/PyScoutFM/assets/9512444/c848f171-02f1-414b-9fdd-a986bd2c7567">
</div>

### Generating the Scout Report

The tool comes with a default [config](src/pyscoutfm/config/config.json) file along with some sensible [attribute weightings](src/pyscoutfm/config/weightings.json) (which were the result of some heavy Machine Learning analysis).

7. In your terminal application run the command:

Cloud:

```
pyscoutfm generate
```

or Local:

```
pyscoutfm generate --import-path=MY_LOCATION --export-path=MY_LOCATION
```

Where `MY_LOCATION` is the path from step 5.

> **Note**: The tool is smart enough to only load the most recent _html_ file in the directory you specify

8. You should see a _Success_ message confirming the generation of the report.

### Using the Scout Report

So you have a Scout Report, now what?

9. _(Optional)_ If you're on the Cloud, download the `latest.html` file from the `OUTPUTS` directory:

<div align="center">
  <img src="https://github.com/olimorris/PyScoutFM/assets/9512444/cf84c98a-536d-41da-8033-9e9ef2890476" alt="Download" />
</div>

10. Open up `latest.html` in your browser and you should see your players from the squad screen alongside their positional ratings which have been calculated with the tool:

<div align="center">
  <img src="https://github.com/olimorris/PyScoutFM/assets/9512444/d6e1c53c-dfbd-4645-9314-04590d09ef71" alt="The scout
    report" />
</div>

11. Clicking on the arrows next to the column headings allows you to sort by that column. Also, a helpful search box makes it easier to find specific players.

12. Each of the rating columns represents a score out of 100. That is, how well suited a player is to a particular position based on the attribute weightings defined in the default [weightings file](src/pyscoutfm/config/weightings.json)

### Hints and Tips

You may find yourself tweaking your search results in Football Manager and re-generating scouting reports often. Below are some tips for doing this optimally:

1. Always export your Football Manager data to the same location. The tool is smart enough to be able to load the most recent HTML file in a directory if you don't pass it an `import_path` parameter.

2. You don't need to re-type your command in the Command Prompt/Terminal. Instead use the <kbd>Up</kbd> key to scroll through historical commands.

3. Once the report has been generated, just refresh the webpage in the Browser. The tool will always overwrite the `latest.html`. Don't worry though...it also saves a datetime stamped copy of the report as well.

## 🚀 Commands

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

### Copy Views

    Usage: pyscoutfm copy-views-to [OPTIONS]

    Copy the included views to a specified path before importing into FM

    Options:
    --path  -p      TEXT  The paths to copy the views to
    --help                Show this message and exit.

### Generate

    Usage: pyscoutfm generate [OPTIONS]

    Generate a scouting report from the data exported from FM

    Options:
    --config-path         TEXT  The path to the config file to use
    --import-path         TEXT  The path to the directory to import from [default: None]
    --export-path         TEXT  The path to the directory to export to [default: None]
    --weightings-path     TEXT  The path to the weightings file to use [default: None]
    --weightings-set      TEXT  The weightings set to use [default: None]
    --help                      Show this message and exit.

## 🔨 Advanced usage

To be updated

## 🔭 How does it work?

To be updated

## ⁉️ FAQs

**Q. Why should I use PyScoutFM over Genie Scout?**
A. I think it comes down to your workflow and how you play the game. I am on a Mac mostly which doesn't help when it comes to using Genie Scout. I also like to use custom weightings which are easier to update with PyScoutFM. Finally, I _think_ the ratings that come out of PyScoutFM are more accurate than Genie Scout's defaults.

**Q. How does PyScoutFM differ to Squirrel's web app and which is better?**
A. Firstly, huge props to Squirrel for starting this _movement_ with Python and Football Manager. I disagreed with how they've setup their weighting/rating system in their tool and valued the work and analysis that had taken place over on [FM-Arena's](https://fm-arena.com/thread/1949-fm22-positional-filters-what-are-the-best-attributes-for-each-position) site. As such, I think that PyScoutFM produces more accurate outputs...and even if you don't think so, you can very quickly change the [weightings](src/pyscoutfm/config/weightings.json) to your liking.

I've put together a comparison table between the two apps:

| Feature | PyScoutFM | Squirrel's |
| --- | :---: | :---: |
| Online web application | ❌ | ✅ |
| Import HTML from Football Manager | ✅ | ✅ |
| HTML output | ✅ | ✅ |
| Number of player roles/positions in the output file | Unlimited | 8 |
| Ratings by role* | ❌ | ✅ |
| Ratings by position | ✅ | ❌ |
| Ratings are a score out of... | 100 | 20 |
| Customisable weightings | ✅ | ❌ |
| Evidence for weightings** | [Here](https://fm-arena.com/find-comment/11228/) | [Here](https://youtu.be/DvV9Aigngi8?t=377) |
| Customisable player positions | ✅ | ❌ |
| Customisable attribute groupings*** | ✅ | ❌ |
| Customisable columns in the output file | ✅ | ❌ |

\* This isn't in PyScoutFM by default but can be added in manually.

\** For PyScoutFM this is a little convoluted but the work done by [Mark](https://fm-arena.com/profile/912-mark/) to produce a balanced filter for Genie Scout was translated into the [default weightings](src/pyscoutfm/config/weightings.json) file.

\*** I like to create a [club DNA](https://www.youtube.com/watch?v=O-F5qI0fI3A) for my saves and this feature allows me to group and weight particular attributes together to produce a DNA rating.
