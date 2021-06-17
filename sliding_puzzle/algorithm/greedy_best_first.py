# -*- coding: utf-8 -*-

from __future__ import annotations

from sliding_puzzle.algorithm import BestFirst


class GreedyBestFirst(BestFirst):
    """
    Implementation of the interface Search with the Greedy Best First algorithm.
    """

    def __repr__(self) -> str:
        return "Greedy Best-First Search"

    def get_new_path(self, move, path):
        """Define the function f(n) used for the implementation of a Best First algorithm

        f(n) = h(n) where h(n) is the heuristic

        :param move: a child of the puzzle on which we want to have its function f (n)
        :type move: Puzzle
        :param path: Path to reach this Puzzle
        :return: the new path according to the function f(n)
        """
        return [self.heuristic.compute(move)] + path[1:] + [move]
