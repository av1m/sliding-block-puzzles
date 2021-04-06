# coding: utf-8
from abc import abstractmethod, ABC
from typing import List

from representation.puzzle import Puzzle


class Search(ABC):
    """
    Interface allowing to find a solution (if possible) in order to solve a Puzzle
    The purpose of this interface is to allow the implementation of different algorithms
    To write an algorithm, just implement this class and override the solve method
    """

    def __init__(self, initial_puzzle: Puzzle):
        self.expanded_nodes: int = ...
        self.solution: List = ...
        self.puzzle: Puzzle = initial_puzzle

    @abstractmethod
    def solve(self) -> None:
        """
        Allows to solve a `Puzzle` by indicating the solution found.
        :return: None. Updates the value of the attributes of the class
        """
        return
