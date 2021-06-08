# coding: utf-8
import logging
from abc import abstractmethod, ABC
from typing import List, final, Union

from sliding_puzzle import Puzzle

logger = logging.getLogger(__name__)


class Search(ABC):
    """
    Interface allowing to find a solution (if possible) in order to solve a Puzzle
    The purpose of this interface is to allow the implementation of different algorithms
    To write an algorithm, just implement this class and override the solve method
    """

    def __init__(self, init_puzzle: Puzzle):
        self.expanded_nodes: int = ...
        self.complexity_memory: int = ...
        self.solution: List[Puzzle] = ...
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
        """Determine if a Puzzle has a solution

        Attention, this function uses the desired goal state of the puzzle passed in parameters.
        The same puzzle with a different goal state can lead to different results

        We count the number of inversions of the Puzzle.
        To count the inversions, we transform our Puzzle in 1D to facilitate the count

        We retrieve the position of the white box in the puzzle and in its goal state
        Then we calculate the distance.
        Finally, we see if the distance (which we have just calculated) and the number of inversions are even or odd

        To have example Puzzle tests and test their solvency, you can look in the tests file

        :param puzzle: the puzzle where we want to test the solvency
        :type puzzle: Puzzle
        :return: True if the puzzle is solvable
        :rtype: bool
        """
        # We transform our puzzle into 1D (need for the inversions)
        puzzle1d: List[int] = Puzzle.to1D(puzzle)
        solved1d: List[int] = Puzzle.to1D(puzzle.GOAL_STATE)
        # Calculation of the number of inversions
        inversions: int = sum(
            1
            for i in range(len(puzzle) ** 2 - 1)
            for j in range(i + 1, len(puzzle) ** 2)
            if solved1d.index(puzzle1d[i]) > solved1d.index(puzzle1d[j])
        )
        # Recovery the index of 0 in the puzzle and in the solved puzzle
        puzzle_blank = puzzle.get_index(puzzle.BLANK)
        solved_blank = puzzle.get_index(puzzle.BLANK, puzzle.GOAL_STATE)
        distance = abs(puzzle_blank[0] - solved_blank[0]) + abs(
            puzzle_blank[1] - solved_blank[1]
        )

        if (distance % 2 == 0 and inversions % 2 == 0) or (
            distance % 2 == 1 and inversions % 2 == 1
        ):
            return True
        return False
