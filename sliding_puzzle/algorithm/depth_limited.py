# coding: utf-8

from sliding_puzzle import Puzzle
from sliding_puzzle.algorithm import Search, DepthLimitedError


class DepthLimited(Search):
    """
    This class implement the interface Search with the Depth Limited Tree Search (and no Graph Search) algorithm.
    """

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
        self.expanded_nodes = 0  # counter of expanded nodes
        self.complexity_memory = 1
        self.solution = []  # initialize the path of the solution
        result = self._recursive(
            puzzle=self.puzzle, limit=self.limit, complexity_memory=1
        )
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

    def _recursive(
        self, puzzle: Puzzle, limit: int, complexity_memory: int
    ) -> DepthLimitedError or None:
        """
        This method return:
        - a list of solution non empty in case of success
        - a list of empty solution in case of cutoff
        - an error in in the event that the algorithm returns failure.
            This case is not supposed to happen, see Search.is_solvable()
        :param puzzle: The puzzle on which we want to apply the DLS
        :type puzzle: Puzzle
        :param limit: the maximum depth of the search
        :type limit: int
        :param complexity_memory: the complexity memory of the solution
        :type complexity_memory: int
        :return: a solution through `solution` attribute or raise an exception if there is a failure
        :rtype: DepthLimitedError or None
        """
        if puzzle.is_goal():
            self.solution.append(puzzle)
            return
        elif limit == 0:  # limit reached
            return DepthLimitedError.CUTOFF
        else:
            cut = False
            move: Puzzle
            for (
                move
            ) in puzzle.get_possible_actions():  # generation of the sons of the node
                self.complexity_memory = max(self.complexity_memory, complexity_memory)
                result = self._recursive(
                    move, limit - 1, complexity_memory + 1
                )  # recursive call with limit decrease by one
                if result == DepthLimitedError.CUTOFF:
                    cut = True
                elif result != DepthLimitedError.FAILURE:
                    self.solution.append(puzzle)
                    return
            if cut:
                return DepthLimitedError.CUTOFF
            else:
                return DepthLimitedError.FAILURE
