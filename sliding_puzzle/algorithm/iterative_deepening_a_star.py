# -*- coding: utf-8 -*-

from __future__ import annotations

from sliding_puzzle import Puzzle, Heuristic, HeuristicLinearConflicts
from sliding_puzzle.algorithm import IterativeLengthening, DepthLimitedError


class IterativeDeepeningAStar(IterativeLengthening):
    """
    Implementation of the interface Search with the Iterative Deepening AStar algorithm.
    """

    def __init__(
        self, init_puzzle: Puzzle, heuristic: Heuristic = HeuristicLinearConflicts
    ) -> None:
        """Initialize the class

        :param init_puzzle: the puzzle we want to solve.
        :type init_puzzle : Puzzle
        :param heuristic: the heuristic we want to use to solve the puzzle
        :type heuristic : Heuristic
        """
        super().__init__(init_puzzle)
        self.heuristic = heuristic
        self.cost_sup_limit = []

    def __repr__(self) -> str:
        return "Iterative Deepening A* Search"

    def _check_cost(self, puzzle: Puzzle, limit_cost: int) -> bool:
        return (puzzle.cost + self.heuristic.compute(puzzle)) > limit_cost

    def _append_cost(self, puzzle: Puzzle) -> None:
        self.cost_sup_limit.append(puzzle.cost + self.heuristic.compute(puzzle))

    def solve(self) -> None:
        """This method solve the puzzle and save the path to do it.
        It return nothing, but fill in self.solution with the good path.
        """
        result = DepthLimitedError.CUTOFF
        self.solution = []
        self.expanded_nodes = 0  # counter of expanded nodes
        self.complexity_memory = 1
        # the limit is the estimation of the cost min to solve the puzzle
        limit_cost = self.heuristic.compute(self.puzzle)
        self.cost_sup_limit.append(limit_cost)
        while result:  # while no solution
            result = self._recursive(self.puzzle, int(limit_cost), 1)
            # the new limit is the cost min reach during the iteration
            limit_cost = min(self.cost_sup_limit)
            self.cost_sup_limit = []
        self.solution.reverse()
