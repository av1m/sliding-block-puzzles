# coding: utf-8
from typing import List

from sliding_puzzle import Puzzle, HeuristicLinearConflicts, Heuristic
from sliding_puzzle.algorithm.search import Search


class GreedyBestFirst(Search):
    """
    Implementation of the interface Search with the Greedy Best First algorithm.
    """

    def __init__(
        self, init_puzzle: Puzzle, heuristic: Heuristic = HeuristicLinearConflicts
    ):
        """Initialize the class
        :param init_puzzle: the puzzle we want to solve.
        :type init_puzzle : Puzzle
        :param heuristic: the heuristic we want to use to solve the puzzle
        :type heuristic : Heuristic
        """
        super().__init__(init_puzzle)
        self.heuristic = heuristic

    def __str__(self):
        return "Greedy Best-First Search"

    def solve(self) -> None:
        """
        This method solve the puzzle and save the path to do it.
        It return nothing, but fill in self.solution with the good path.
        """
        queue: List = [
            [self.heuristic.compute(self.puzzle), self.puzzle]
        ]  # initialization of the border
        expanded = []  # list of nodes expanded
        self.expanded_nodes = 0  # counter of expanded nodes
        while queue:
            i = 0
            for j in range(1, len(queue)):
                if queue[i][0] > queue[j][0]:  # minimum
                    i = j
            path = queue[i]
            queue = (
                queue[:i] + queue[i + 1 :]
            )  # deletion of the path to the current node in the border
            node = path[-1]  # current node (last element of the path)
            if node.is_goal():
                self.solution = path[1:]
                self.complexity_memory = len(queue) + self.expanded_nodes
                return
            expanded.append(node.tiles)
            self.expanded_nodes += 1
            move: Puzzle
            for (
                move
            ) in node.get_possible_actions():  # generation of the sons of the node
                if not ((move.tiles in expanded) or move in [x[-1] for x in queue]):
                    new_path = [self.heuristic.compute(move)] + path[1:] + [move]
                    queue.append(new_path)
                elif move in [
                    x[-1] for x in queue
                ]:  # check if node is already in the border
                    ind = [x[-1] for x in queue].index(move)
                    if queue[ind][0] > self.heuristic.compute(
                        move
                    ):  # we remplace it if it has a better cost
                        queue.pop(ind)
                        queue.append(path + [move])
