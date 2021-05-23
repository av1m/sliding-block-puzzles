# coding=utf-8
from sliding_puzzle import Puzzle
from sliding_puzzle.algorithm import *

if __name__ == "__main__":
    puzzle: Puzzle = Puzzle(
        [[4, 1, 2, 3], [5, 6, 7, 11], [8, 9, 10, 15], [12, 13, 14, 0]],
        # [[3, 1, 2], [0, 4, 5], [6, 7, 8]]
    )
    a_star: AStar = AStar(puzzle)
    a_star.solve()
    for step in a_star.solution:
        print("{}  Cost ==> {}\n".format(step, step.cost))
    print(a_star.expanded_nodes)
