# coding: utf-8

from typing import Protocol, List

from representation.puzzle import Puzzle


class Search(Protocol):
    def __init__(self, init_puzzle: Puzzle):
        self.expanded_nodes: int = ...
        self.solution: List = ...
        self.puzzle: Puzzle = init_puzzle

    def solve(self) -> None:
        ...
