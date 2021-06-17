# -*- coding: utf-8 -*-

from __future__ import annotations

from sliding_puzzle.algorithm import BestFirst


class AStar(BestFirst):
    """
    Implementation of the interface Search with the AStar algorithm.
    """

    def __repr__(self) -> str:
        return "A* Search"

    def get_new_path(self, move, path):
        """Define the function f(n) used for the implementation of a Best First algorithm

        f(n) = h(n) + g(n)
        where h(n) is the heuristic and g(n) the cost

        :param move: a child of the puzzle on which we want to have its function f (n)
        :type move: Puzzle
        :param path: Path to reach this Puzzle
        :return: the new path according to the function f(n)
        """
        return [self.heuristic.compute(move) + move.cost] + path[1:] + [move]
