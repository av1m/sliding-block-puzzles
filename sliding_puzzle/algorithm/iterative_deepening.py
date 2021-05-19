# coding: utf-8
from sliding_puzzle import Puzzle
from sliding_puzzle.algorithm import DepthLimited
from sliding_puzzle.algorithm.depth_limited import DepthLimitedError


class IterativeDeepening(DepthLimited):
    def __init__(self, init_puzzle: Puzzle, limit: int = 5, step: int = 3):
        super().__init__(init_puzzle, limit)
        self.step = step

    def __repr__(self):
        return "Iterative Deepening Depth-First Search"

    def solve(self) -> None:
        result = DepthLimitedError.CUTOFF
        self.solution = []
        self.expanded_nodes = 0
        while result:
            result = self._recursive(self.puzzle, self.limit)
            self.limit += self.step
        self.solution.reverse()
