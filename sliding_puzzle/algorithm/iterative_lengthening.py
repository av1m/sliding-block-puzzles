# coding: utf-8
# from typing import List
from sliding_puzzle import Puzzle
from sliding_puzzle.algorithm import DepthLimitedError
from sliding_puzzle.algorithm.search import Search


class IterativeLengthening(Search):
    """
    Implementation of the interface Search with the Iterative Lengthening algorithm.
    """

    def __init__(self, init_puzzle: Puzzle):
        """
        Initialize the class
        :param init_puzzle: the puzzle we want to solve.
        :type init_puzzle : Puzzle
        """
        super().__init__(init_puzzle)
        self.cost_sup_limit = []

    def __str__(self):
        return "IterativeLengthening"

    def solve(self) -> None:
        """
        This method solve the puzzle and save the path to do it.
        It return nothing, but fill in self.solution with the good path.
        """
        result = DepthLimitedError.CUTOFF
        self.solution = []
        self.expanded_nodes = 0  # counter of expanded nodes
        limit_cost = 0
        while result:  # while no solution
            result = self.recursive(self.puzzle, limit_cost)
            limit_cost = min(
                self.cost_sup_limit
            )  # the new limit is the cost min reach during the iteration
            self.cost_sup_limit = []
        self.solution.reverse()

    def recursive(self, puzzle: Puzzle, limit_cost: int) -> DepthLimitedError or None:
        """
        This method return:
        - a list of solution non empty in case of success
        - a list of empty solution in case of cutoff
        - an error in in the event that the algorithm returns failure.
            This case is not supposed to happen, see Search.is_solvable()
        :param puzzle: The puzzle on which we want to apply IDA*
        :type puzzle: Puzzle
        :param limit_cost: the maximum depth of the search
        :type limit_cost: int
        :return: a solution through `solution` attribute or raise an exception if there is a failure
        :rtype: DepthLimitedError or None
        """
        if puzzle.is_goal():
            self.solution.append(puzzle)
            return
        elif puzzle.cost > limit_cost:
            self.cost_sup_limit.append(puzzle.cost)
            return DepthLimitedError.CUTOFF
        else:
            cut = False
            for (
                move
            ) in puzzle.get_possible_actions():  # generation of the sons of the node
                result = self.recursive(move, limit_cost)
                if result == DepthLimitedError.CUTOFF:
                    cut = True
                elif result != DepthLimitedError.FAILURE:
                    self.solution.append(puzzle)
                    return
            if cut:
                return DepthLimitedError.CUTOFF
            else:
                return DepthLimitedError.FAILURE
