# Sliding block puzzles

[![Sliding Puzzle CI](https://github.com/av1m/sliding-block-puzzles/actions/workflows/actions.yaml/badge.svg)](https://github.com/av1m/sliding-block-puzzles/actions/workflows/actions.yaml)

## Usage

At this stage, you can use the project in different ways:

1. In a python script, consult the [sample](sample/) directory for an example
2. Run the CLI with the command ```python -m sliding_puzzle``` _(maybe you need to make `source .venv/bin/activate`)_
   Simple command
   ```shell
   python3 -m sliding_puzzle --tiles 1 3 2 4 0 7 5 8 6 --method a_star
   ```
   More complex
   ```shell
   python3 -m sliding_puzzle \
     --verbose \
     --tiles 4 1 2 3 5 6 7 11 8 9 10 15 12 13 14 0 \
     --method a_star depth_limited \
     --no-blank-at-first
   ```
3. Run the server with the command ```make serve```
4. Run a client GUI that request the server (created at 3.) or directly in Python (Flask, Django ...).
   Try an example [writing in Flutter](https://github.com/av1m/slide_puzzle)

## Get started 🚀

1. Install the dependencies
   ```shell
   python -m pip install git+https://github.com/av1m/sliding-block-puzzles
   ```
2. Run an example
   ```shell
   wget -qO- https://raw.githubusercontent.com/av1m/sliding-block-puzzles/master/sample/simple.py | python -
   ```
3. Run the CLI
   ```shell
   python -m sliding_puzzle
   ```

## Developers 👨‍💻

Use `python3` or `python` command (depending on your configuration)

1. Clone this project
   ```shell
   git clone https://github.com/av1m/sliding-block-puzzles
   cd src-puzzles
   ```
2. Run make command
   ```shell
   make install
   ```

Everything has been installed and configured correctly! 🎉
