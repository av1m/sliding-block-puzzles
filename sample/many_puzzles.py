# -*- coding: utf-8 -*-
from sliding_puzzle import Puzzle
from sliding_puzzle.algorithm import *

if __name__ == "__main__":
    puzzles = [
        # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12], [13, 14, 15, 11]],
        # [[4, 1, 2, 3], [5, 6, 7, 11], [8, 9, 10, 15], [12, 13, 14, 0]],
        [[0, 1, 2], [4, 5, 3], [7, 8, 6]],
        [[1, 2, 3], [0, 4, 6], [7, 5, 8]],
        [[1, 0, 3], [7, 2, 5], [8, 4, 6]],
    ]

    for _puzzle in puzzles:
        print("---")
        puzzle = Puzzle(_puzzle)
        for strategy in [GreedyBestFirst]:
            strategy = strategy(puzzle)
            strategy.solve()
            print(
                "{0} - Expanded Nodes: {1} \n{0} - Cost: {2}".format(
                    strategy, strategy.expanded_nodes, strategy.solution[-1].cost
                )
            )
