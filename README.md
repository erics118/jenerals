# jenerals.io

[generals.io](https://generals.io) clone in python using `cmu_graphics`.

## Requirements

This requires `Python 3.10`.

## Installation

After cloning, install the required packages with `pip install -e .`.
See `pyproject.toml` for the list of required packages.

## Running

Run primary player with `python3 src/main.py --primary`. On the same local network (on the same computer or a different computer), run secondary player with `python3 src/main.py --secondary --code {code}`. `{code}` is the "Room Code" that is printed to the console on the primary player's screen.

You must start the primary player's game first, then start secondary player's game. If you start the secondary player's game first, it will not work. Currently, you must start both games almost immediately after each other, or else the secondary player will be out of sync.

It is also possible to play the game with one player. Just run with `--dev --primary` and press `shift-v` (`V`) to toggle visibility of all cells. See controls specified under [Dev Shortcuts](#dev-shortcuts).

## Project Proposal

Project proposal documents are located under `proposal/`

## Game Mechanics

This game is relatively simple compared to a lot of other games. The goal is to gather troops (numbers in the center of a cell) to take over the opponent's general (cell with a crown).

There are mountains blocking the path, and cities which take 40-50 troops to capture but produce troops at a much faster rate.

Generals and cities produce troops once per second, other cells produce troops once every 25 seconds. You can move two times per second.

At all times, there is at least one troop in a cell that you control.

## Controls

`arrow keys` - Premove the selected cell, and the troops on it.

`q` - Clear all premoves.

`e` - Undo the latest premove.

`space` - Toggle moving troops when moving the selected cell.

## Dev Shortcuts

Run the program in development mode with the `--dev` flag. This enables some features that are not part of the original [generals.io](https://generals.io) game.

`shift-f` `F` - Toggle flag. For debugging, has no effect on gameplay.

`shift-v` (`V`) - Toggle visibility of all cells.

Additionally, if there is only a primary player, there are some additional shortcuts:

`wasd` - Move the opponent's selected cell.

`z` - Clear the opponent's premoves.

`x` - Undo the opponent's latest premove.

`c` - Toggle moving troops when moving the opponent's selected cell.

`shift-,` (`<`) - Step by one turn.

`shift-.` (`>`) - Step 25 turns.

`shift-/` (`?`) - Do all premoves for both players

`shift-p` (`P`) - Pause/unpause the game.
