# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import logging
import math
from typing import Callable

from sliding_puzzle import TypePuzzle, Puzzle
from sliding_puzzle.algorithm import get_algorithm, Search

logger = logging.getLogger(__name__)


class CLI:
    """
    Class used to use the sliding_puzzle package from the command line

    Example::

        You can add "python3 -m" in front of sliding_puzzle

        # Simple command
        sliding_puzzle --tiles 1 3 2 4 0 7 5 8 6 --method a_star

        # More complex
        sliding_puzzle \
            --verbose \
            --tiles 4 1 2 3 5 6 7 11 8 9 10 15 12 13 14 0 \
            --method a_star depth_limited \
            --no-blank-at-first
    """

    def __init__(self) -> None:
        _parser: argparse.ArgumentParser = argparse.ArgumentParser(
            prog="sliding_puzzle",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description="Usage example:\n"
            "Basic  : python3 -m sliding_puzzle "
            "--tiles 1 3 2 4 0 7 5 8 6 "
            "--method a_star\n"
            "Complex: python3 -m sliding_puzzle "
            "--verbose "
            "--tiles 4 1 2 3 5 6 7 11 8 9 10 15 12 13 14 0 "
            "--method a_star depth_limited "
            "--no-blank-at-first",
            epilog="For every --OPTION there is also a --no-OPTION that reverts OPTION to its default value.",
        )
        _parser.add_argument(
            "-v",
            "--verbose",
            help="Verbose output",
            default=False,
            action=argparse.BooleanOptionalAction,
        )
        _required = _parser.add_argument_group(title="Required Arguments")
        _required.add_argument(
            "--method",
            required=True,
            help="Algorithm used",
            nargs="*",
            choices=get_algorithm.keys(),
        )
        _required.add_argument(
            "--tiles",
            required=True,
            help="The puzzle by putting spaces. For example '1 2 3 4 5 6 7 8 0'",
            nargs="*",
        )
        _required.add_argument(
            "--blank-at-first",
            required=False,
            help="Determines the place of the BLANK: first or last",
            default=True,
            action=argparse.BooleanOptionalAction,
        )
        self.args: argparse.Namespace = _parser.parse_args()

    def parse_tiles(self) -> TypePuzzle:
        """Parse the input to a list exploitable by the Puzzle class

        :return: a list of tiles ready to be used by Puzzle
        :rtype: TypePuzzle
        """
        tiles: list[int] = [int(t) for t in self.args.tiles]
        sqrt_tiles = int(math.sqrt(len(self.args.tiles)))
        return [tiles[x : x + sqrt_tiles] for x in range(0, len(tiles), sqrt_tiles)]

    def parse_method(self) -> list[Callable[..., Search]]:
        """Get the algorithm the user wants to use

        :return: the list of all the algorithms that the user wishes to re-mail on his puzzle.
            This list is callable.
        :rtype: List[Callable[..., Search]]
        """
        return [get_algorithm.get(method) for method in self.args.method]

    def run(self) -> None:
        """Starts the command line interface
        Print only on the terminal
        """
        puzzle: Puzzle = Puzzle(self.parse_tiles(), self.args.blank_at_first)
        for strategy in self.parse_method():
            strategy = strategy(puzzle)
            strategy.solve()
            print("{0} - Expanded Nodes: {1}".format(strategy, strategy.expanded_nodes))
            for step in strategy.solution:
                print(step)
