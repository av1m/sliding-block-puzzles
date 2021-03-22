# coding: utf-8

from typing import Protocol, List


class Search(Protocol):
    def __init__(self):
        self.expanded_nodes: int = ...
        self.solution: List = ...

    def solve(self) -> None:
        ...
