# coding: utf-8

from sliding_puzzle import Puzzle
from sliding_puzzle.algorithm import Search, DepthLimitedError


class DepthLimited(Search):
    def __init__(self, init_puzzle: Puzzle, limit: int = 5):
        super().__init__(init_puzzle)
        self.limit = limit

    def __repr__(self):
        return "Depth-Limited Search"

    def solve(self) -> None:
        """
        This method return:
        - a list of solution non empty in case of success
        - a list of empty solution in case of cutoff
        - an error in in the event that the algorithm returns failure.
            This case is not supposed to happen, see Search.is_solvable()

        :return: a solution through `solution` attribute or raise an exception if there is a failure
        :rtype: None
        """
        self.expanded_nodes = 0
        self.solution = []
        result = self._recursive(self.puzzle, self.limit)
        if not result:  # We have a solution
            self.solution.reverse()
        elif result == DepthLimitedError.CUTOFF:
            assert not self.solution  # no solution
            return
        elif result == DepthLimitedError.FAILURE:
            raise Exception(
                "This problem can't be solved, check the Search.is_solvable()"
            )
        return

    def _recursive(self, puzzle: Puzzle, limit: int) -> DepthLimitedError or None:
        if puzzle.is_goal():
            self.solution.append(puzzle)
            return
        elif limit == 0:
            return DepthLimitedError.CUTOFF
        else:
            cut = False
            for move in puzzle.get_possible_actions():
                result = self._recursive(move, limit - 1)
                if result == DepthLimitedError.CUTOFF:
                    cut = True
                elif result != DepthLimitedError.FAILURE:
                    self.solution.append(puzzle)
                    return
            if cut:
                return DepthLimitedError.CUTOFF
            else:
                return DepthLimitedError.FAILURE
