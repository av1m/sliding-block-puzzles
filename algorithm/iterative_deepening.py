# coding: utf-8

from algorithm.search import Search
from representation.puzzle import Puzzle


class IterativeDeepening(Search):
    def __init__(self, init_puzzle: Puzzle):
        super().__init__(init_puzzle)

    def solve(self) -> None:
        ...
