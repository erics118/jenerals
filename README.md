# jenerals.io

generals.io clone in python using cmu_graphics

## Installation

Install `Python 3.10` using your package manager. Any patch version should work. Other minor versions may work, but this is the only one that is tested.

Install the `cairo` graphics library using your package manager, as it is required by the `cmu_graphics` dependency.

Install the required packages with `pip install -e .`.

## Running

Run the program with `python3 src/main.py`

Run the program in development mode with `python3 src/main.py --dev`

## Just

If you have [`just`](https://github.com/casey/just) installed, there are some other shortcuts.

You can run `just install` to install the required packages.

You can also use `just run` to run the program.

Use `just dev` to run the program in development mode, which includes a few extra features to help with development.

## Project Proposal

Project proposal documents are located under `proposal/`

## Dev Shortcuts

`F` - toggle flag (for debugging)

`<` - step one turn

`>` - step 25 turns

`?` - do all premoves

`P` - pause the game

`V` - toggle visibility of all squares

`C` - collect all troops into a single squares
