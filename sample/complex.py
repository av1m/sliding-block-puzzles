# coding=utf-8

from __future__ import annotations

from typing import List, TypeVar

from sliding_puzzle import Puzzle, TypePuzzle
from sliding_puzzle.algorithm import get_algorithm

if __name__ == "__main__":
    puzzles: List[TypePuzzle] = [
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12], [13, 14, 15, 11]],
        [[4, 1, 2, 3], [5, 6, 7, 11], [8, 9, 10, 15], [12, 13, 14, 0]],
        [[0, 1, 2], [4, 5, 3], [7, 8, 6]],
        [[1, 2, 3], [0, 4, 6], [7, 5, 8]],
        [[1, 0, 3], [7, 2, 5], [8, 4, 6]],
    ]

    SearchType = TypeVar("SearchType", bound="Search")

    for _puzzle in puzzles:
        print("---")
        puzzle: Puzzle = Puzzle(_puzzle)
        for strategy_name, strategy in get_algorithm.items():
            strategy = strategy(puzzle)
            strategy.solve()
            print(
                "{0} - Expanded Nodes: {1} \n{0} - Cost: {2}".format(
                    strategy, strategy.expanded_nodes, strategy.solution[-1].cost
                )
            )
