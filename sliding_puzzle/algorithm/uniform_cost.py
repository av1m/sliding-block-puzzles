# coding: utf-8
from typing import List, Union

from sliding_puzzle import Puzzle
from sliding_puzzle.algorithm import Search


class UniformCost(Search):
    """
    Implementation of the interface Search with the Uniform Cost algorithm.
    """

    def __repr__(self):
        return "Uniform-Cost Search"

    def solve(self) -> None:
        """
        This method solve the puzzle and save the path to do it.
        It return nothing, but fill in self.solution with the good path.
        """
        queue = [[self.puzzle]]  # initialization of the border
        expanded = []  # list of nodes expanded
        self.expanded_nodes = 0  # counter of expanded nodes
        while queue:
            cost_min: List[Union[Puzzle, int]] = Search.get_min_cost(
                queue
            )  # list sorted by cost
            node: Puzzle = cost_min[0]  # get minimum cost
            index: int = cost_min[1]
            path = queue.pop(
                index
            )  # deletion of the path to the current node in the border
            if node.is_goal():
                self.solution = path
                return
            expanded.append(node.tiles)
            self.expanded_nodes += 1
            for (
                move
            ) in node.get_possible_actions():  # generation of the sons of the node
                if not ((move.tiles in expanded) or move in [x[-1] for x in queue]):
                    queue.append(path + [move])
                elif move in [
                    x[-1] for x in queue
                ]:  # check if node is already in the border
                    ind = [x[-1] for x in queue].index(move)
                    if (
                        queue[ind][-1].cost > move.cost
                    ):  # we replace it if it has a better cost
                        queue.pop(ind)
                        queue.append(path + [move])
