# coding=utf-8

from algorithm.a_star import AStar
from algorithm.breadth_first import BreadthFirst
from representation.puzzle import Puzzle

if __name__ == "__main__":
    puzzle: Puzzle = Puzzle([[3, 1, 2], [4, 5, 8], [6, 7, 0]])
    print(puzzle)

    for strategy in [AStar, BreadthFirst]:
        strategy = strategy(puzzle)
        print(strategy.__dict__)
        strategy.solve()
        print("{0} - Expanded Nodes: {1}".format(strategy, strategy.expanded_nodes))
        for _ in strategy.solution:
            print(_)
