# coding: utf-8
from abc import abstractmethod, ABC
from typing import List

from representation.puzzle import Puzzle, TypePuzzle


class Search(ABC):
    """
    Interface allowing to find a solution (if possible) in order to solve a Puzzle
    The purpose of this interface is to allow the implementation of different algorithms
    To write an algorithm, just implement this class and override the solve method
    """

    def __init__(self, init_puzzle: Puzzle):
        self.expanded_nodes: int = ...
        self.solution: List[TypePuzzle] = ...
        self.puzzle: Puzzle = init_puzzle

    @abstractmethod
    def solve(self) -> None:
        """
        Allows to solve a `Puzzle` by indicating the solution found.
        :return: None. Updates the value of the attributes of the class
        """
        return

    @staticmethod
    def get_min_cost(queue: List[List[Puzzle]]):
        """
        Allows you to search for the Puzzle that has the minimum cost in a Puzzle list list
        Get the last element of each sublist then sort according to the minimum cost
        This function does not modify the queue list

        Example::

            queue = [[
                    Puzzle(tiles=[[3, 1, 2], [0, 4, 5], [6, 7, 8]], cost=2),
                ],[
                    Puzzle(tiles=[[3, 1, 2], [0, 4, 5], [6, 7, 8]], cost=4),
                    Puzzle(tiles=[[3, 1, 2], [4, 0, 5], [6, 7, 8]], cost=1)
                ],[
                    Puzzle(tiles=[[3, 1, 2], [0, 4, 5], [6, 7, 8]], cost=6),
                    Puzzle(tiles=[[3, 1, 2], [6, 4, 5], [0, 7, 8]], cost=5),
                    Puzzle(tiles=[[3, 8, 2], [6, 4, 5], [0, 7, 1]], cost=2)
            ]]

            get_min_cost(queue) will return a list where :
                - [0] = Puzzle(tiles=[[3, 1, 2], [4, 0, 5], [6, 7, 8]], cost=1)
                - [1] = 1

        :param queue: Puzzle List List
        :return: list with two elements. At index 0, is the Puzzle.
            At index 1, is the index of the sublist where the minimum cost puzzle was found
        """
        return sorted(
            [[x[-1], index] for index, x in enumerate(queue)],
            key=lambda list_: list_[0],
        )[0]
