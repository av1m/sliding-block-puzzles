# coding: utf-8
from __future__ import annotations

import argparse
import logging
import math
from typing import List, Callable

from sliding_puzzle.algorithm import get_algorithm
from sliding_puzzle.algorithm.search import Search
from sliding_puzzle.representation.puzzle import TypePuzzle, Puzzle

logger = logging.getLogger(__name__)


class CLI:
    def __init__(self):
        _parser = argparse.ArgumentParser(
            prog="sliding_puzzle",
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
        self.args = _parser.parse_args()

    def parse_tiles(self) -> TypePuzzle:
        tiles = [int(t) for t in self.args.tiles]
        sqrt_tiles = int(math.sqrt(len(self.args.tiles)))
        return [tiles[x : x + sqrt_tiles] for x in range(0, len(tiles), sqrt_tiles)]

    def parse_method(self) -> List[Callable[..., Search]]:
        return [get_algorithm.get(method) for method in self.args.method]

    def run(self):
        puzzle: Puzzle = Puzzle(self.parse_tiles())
        for strategy in self.parse_method():
            strategy = strategy(puzzle)
            strategy.solve()
            print("{0} - Expanded Nodes: {1}".format(strategy, strategy.expanded_nodes))
            for step in strategy.solution:
                print(step)
