# coding=utf-8

from algorithm.a_star import AStar
from representation.puzzle import Puzzle

if __name__ == "__main__":
    puzzle: Puzzle = Puzzle(
        [[4, 1, 2, 3], [5, 6, 7, 11], [8, 9, 10, 15], [12, 13, 14, 0]]
    )
    print(puzzle)

    for strategy in [AStar]:
        strategy = strategy(puzzle)
        strategy.solve()
        print("{0} - Expanded Nodes: {1}".format(strategy, strategy.expanded_nodes))
        for _ in strategy.solution:
            print(_)
