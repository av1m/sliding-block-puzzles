# coding: utf-8
# from typing import List
from sliding_puzzle import Puzzle, Heuristic, HeuristicManhattan
from sliding_puzzle.algorithm import DepthLimitedError
from sliding_puzzle.algorithm.search import Search


class IterativeDeepeningAStar(Search):
    def __init__(self, init_puzzle: Puzzle, heuristic: Heuristic = HeuristicManhattan):
        super().__init__(init_puzzle)
        self.heuristic = heuristic
        self.cost_sup_limit = []

    def __str__(self):
        return "IterativeDeepeningAStar"

    def solve(self) -> None:
        result = DepthLimitedError.CUTOFF
        self.solution = []
        self.expanded_nodes = 0
        limit_cost = self.heuristic.compute(self.puzzle)
        while result:
            result = self.recursive(self.puzzle, limit_cost)
            limit_cost = min(self.cost_sup_limit)
            self.cost_sup_limit = []
        self.solution.reverse()

    def recursive(self, puzzle: Puzzle, limit_cost: int) -> DepthLimitedError or None:
        if puzzle.is_goal():
            self.solution.append(puzzle)
            return
        elif (puzzle.cost + self.heuristic.compute(puzzle)) > limit_cost:
            self.cost_sup_limit.append(puzzle.cost + self.heuristic.compute(puzzle))
            return DepthLimitedError.CUTOFF
        else:
            cut = False
            for move in puzzle.get_possible_actions():
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
