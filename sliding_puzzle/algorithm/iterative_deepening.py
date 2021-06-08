# coding: utf-8
from sliding_puzzle import Puzzle
from sliding_puzzle.algorithm import DepthLimited
from sliding_puzzle.algorithm.depth_limited import DepthLimitedError


class IterativeDeepening(DepthLimited):
    """
    Implementation of the interface Search with the Iterative Deepening algorithm.
    """

    def __init__(self, init_puzzle: Puzzle, limit: int = 5, step: int = 3):
        """ Initialize the class
        :param init_puzzle: the puzzle we want to solve.
        :type init_puzzle : Puzzle
        :param limit: the limit max of the depth for the first iteration
        :type limit : int
        :param step: the step who increase the limit at each iteration
        :type step : int
        """
        super().__init__(init_puzzle, limit)
        self.step = step

    def __repr__(self):
        return "Iterative Deepening Depth-First Search"

    def solve(self) -> None:
        """
        This method solve the puzzle and save the path to do it.
        It return nothing, but fill in self.solution with the good path.
        """
        result = DepthLimitedError.CUTOFF
        self.solution = []
        self.expanded_nodes = 0  # counter of expanded nodes
        while result:  # while no solution (so while result is a Depth-Limited Error)
            result = self._recursive(self.puzzle, self.limit)  # call a DLS search
            self.limit += self.step  # increase the limit
        self.solution.reverse()
