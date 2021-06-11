# -*- coding: utf-8 -*-

from __future__ import annotations

from sliding_puzzle import Puzzle
from sliding_puzzle.algorithm import DepthLimitedError
from sliding_puzzle.algorithm.search import Search


class IterativeLengthening(Search):
    """
    Implementation of the interface Search with the Iterative Lengthening algorithm.
    """

    def __init__(self, init_puzzle: Puzzle) -> None:
        """Initialize the class

        :param init_puzzle: the puzzle we want to solve.
        :type init_puzzle : Puzzle
        """
        super().__init__(init_puzzle)
        self.cost_sup_limit = []

    def __repr__(self) -> str:
        return "Iterative Lengthening Search"

    def solve(self) -> None:
        """This method solve the puzzle and save the path to do it.
        It return nothing, but fill in self.solution with the good path.
        """
        result = DepthLimitedError.CUTOFF
        self.solution: list = []
        self.expanded_nodes = 0  # counter of expanded nodes
        self.complexity_memory = 1
        limit_cost = 0
        self.cost_sup_limit.append(limit_cost)
        while result:  # while no solution
            result = self._recursive(self.puzzle, limit_cost, 1)
            # the new limit is the cost min reach during the iteration
            limit_cost = min(self.cost_sup_limit)
            self.cost_sup_limit = []
        self.solution.reverse()

    def _check_cost(self, puzzle: Puzzle, limit_cost: int) -> bool:
        """Check the cost of the puzzle against the limit

        This method seems trivial but it aims to be redefined in a child

        :param puzzle: Puzzle on which we must check the cost
        :type puzzle: Puzzle
        :param limit_cost: Cost limit that the algorithm must not exceed
        :type limit_cost: int
        :return: true if the cost of the puzzle is strictly greater than the limit
        :rtype: bool
        """
        return puzzle.cost > limit_cost

    def _append_cost(self, puzzle: Puzzle) -> None:
        """Add a cost to the list of cost limits

        This method seems trivial but it aims to be redefined in a child

        :param puzzle: puzzle where we get the cost
        :type puzzle: Puzzle
        """
        self.cost_sup_limit.append(puzzle.cost)

    def _recursive(
        self, puzzle: Puzzle, limit_cost: int, complexity_memory: int
    ) -> DepthLimitedError or None:
        """Recursive method used to implement the algorithm

        This method return:
        - a list of solution non empty in case of success
        - a list of empty solution in case of cutoff
        - an error in in the event that the algorithm returns failure.
            This case is not supposed to happen, see Search.is_solvable()

        :param puzzle: The puzzle on which we want to apply IDA*
        :type puzzle: Puzzle
        :param limit_cost: the maximum depth of the search
        :type limit_cost: int
        :param complexity_memory: the complexity memory of the solution
        :type complexity_memory: int
        :return: a solution through `solution` attribute or raise an exception if there is a failure
        :rtype: DepthLimitedError or None
        """
        if puzzle.is_goal():
            self.solution.append(puzzle)
            return
        elif self._check_cost(puzzle=puzzle, limit_cost=limit_cost):
            self._append_cost(puzzle=puzzle)
            return DepthLimitedError.CUTOFF
        else:
            cut = False
            move: Puzzle
            for (
                move
            ) in puzzle.get_possible_actions():  # generation of the sons of the node
                self.complexity_memory = max(self.complexity_memory, complexity_memory)
                result = self._recursive(move, limit_cost, complexity_memory + 1)
                if result == DepthLimitedError.CUTOFF:
                    cut = True
                elif result != DepthLimitedError.FAILURE:
                    self.solution.append(puzzle)
                    return
            if cut:
                return DepthLimitedError.CUTOFF
            else:
                return DepthLimitedError.FAILURE
