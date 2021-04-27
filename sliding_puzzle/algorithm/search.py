# coding: utf-8
import logging
from abc import abstractmethod, ABC
from typing import List, final, Union

from sliding_puzzle import Puzzle, TypePuzzle

logger = logging.getLogger(__name__)


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
        if not self.is_solvable(init_puzzle):
            raise ValueError("The puzzle has no solution")

    @abstractmethod
    def solve(self) -> None:
        """
        Allows to solve a `Puzzle` by indicating the solution found.
        :return: None. Updates the value of the attributes of the class
        """
        return

    @staticmethod
    @final
    def get_min_cost(queue: List[List[Puzzle]]) -> List[Union[Puzzle, int]]:
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
            [[puzzle[-1], index] for index, puzzle in enumerate(queue)],
            key=lambda list_: list_[0],
        )[0]

    @staticmethod
    @final
    def is_solvable(puzzle: Puzzle) -> bool:
        if puzzle.LEN_TILES % 2 != 0:  # odd
            flat_list: List[int] = [
                item
                for sublist in puzzle.tiles
                for item in sublist
                if item != puzzle.BLANK
            ]

            total_inversion: int = sum(
                sum(1 for i in range(index, len(flat_list)) if (flat_list[i] < item))
                for index, item in enumerate(flat_list)
            )
            return total_inversion % 2 == 0
        else:  # even
            permutations = 0
            flat_list = [item for sublist in puzzle.tiles for item in sublist]
            for index in range(len(flat_list)):
                variable = flat_list[index]
                if index != variable:
                    index_var = flat_list.index(index)
                    flat_list[index], flat_list[index_var] = (
                        flat_list[index_var],
                        flat_list[index],
                    )
                    permutations += 1
            i1, j1 = puzzle.get_index(0)
            i2, j2 = Puzzle(puzzle.GOAL_STATE).get_index(
                0
            )  # We retrieve the position of index 0 in the GOAL STATE
            distance = abs(i2 - i1) + abs(j2 - j1)
            return (
                True
                if ((distance % 2 == 0) and (permutations % 2 == 0))
                or ((distance % 2 != 0) and (permutations % 2 != 0))
                else False
            )
