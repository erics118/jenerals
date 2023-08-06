# jenerals.io

generals.io clone in python using cmu_graphics

## Requirements

This requires `Python 3.10` and the `cairo` graphics library.

## Installation

After cloning, install the required packages with `pip install -e .`.

## Running

Run the program with `python3 src/main.py`

## Project Proposal

Project proposal documents are located under `proposal/`

## Dev Shortcuts

Run the program in development mode with `python3 src/main.py --dev`

`F` - toggle flag (for debugging)

`<` - step one turn

`>` - step 25 turns

`?` - do all premoves

`P` - pause the game

`V` - toggle visibility of all squares

## Just

If you have [`just`](https://github.com/casey/just) installed, there are some other shortcuts.

You can run `just install` to install the required packages.

You can also use `just run` to run the program.

Use `just dev` to run the program in development mode, which includes a few extra features to help with development.
