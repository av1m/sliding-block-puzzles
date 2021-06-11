# Sliding block puzzles

[![Sliding Puzzle CI](https://github.com/av1m/sliding-block-puzzles/actions/workflows/actions.yaml/badge.svg)](https://github.com/av1m/sliding-block-puzzles/actions/workflows/actions.yaml)
[![Python3.9](https://img.shields.io/badge/Python-3.9-blue)](https://docs.python.org/3/whatsnew/3.9.html)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/av1m/sliding-block-puzzles/blob/master/LICENSE)

## Usage 📖

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
4. Run a client GUI that request the server (created at 3.) or directly in Python (Flask, Django ...). Try an
   example [writing in Flutter](https://github.com/av1m/slide_puzzle)

## Get started 🎉

Install the dependencies

```shell
python -m pip install git+https://github.com/av1m/sliding-block-puzzles
```

You have now added the dependency, you can:

* Run an example
   ```shell
   wget -qO- https://raw.githubusercontent.com/av1m/sliding-block-puzzles/master/sample/simple.py | python -
   ```
  > 💡 All the examples are in the [`sample/`](./sample/) directory
* Run the CLI
   ```shell
   python -m sliding_puzzle
   ```
* Run the server
   ```shell
   cd sliding_puzzle
   make serve
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
3. Test the project
   ```shell
   make test
   ```

Everything has been installed and configured correctly! 🎉

## Deploy the server 🚀

We use a WSGI server.

It can easily be run and deployed using the command :

```bash
gunicorn sliding_puzzle.wsgi --reload --timeout 1000
```

For example, if you want to deploy to [Heroku](https://heroku.com), you can create a Heroku project. Then, add the
heroku project to this project (through `git remote add`) and run this command

```shell
make deploy
```

> In order to deploy to Heroku, you need a [`Procfile` file](https://devcenter.heroku.com/articles/getting-started-with-python#define-a-procfile)
