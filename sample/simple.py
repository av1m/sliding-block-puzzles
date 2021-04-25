# coding=utf-8
from sliding_puzzle.algorithm import AStar
from sliding_puzzle.representation.puzzle import Puzzle

if __name__ == "__main__":
    puzzle: Puzzle = Puzzle([[3, 1, 2], [0, 4, 5], [6, 7, 8]])
    a_star = AStar(puzzle)
    a_star.solve()
    for step in a_star.solution:
        print(step)
