# -*- coding: utf-8 -*-

from __future__ import annotations

from sliding_puzzle import Puzzle, HeuristicLinearConflicts, Heuristic
from sliding_puzzle.algorithm.search import Search


class GreedyBestFirst(Search):
    """
    Implementation of the interface Search with the Greedy Best First algorithm.
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

    def __repr__(self) -> str:
        return "Greedy Best-First Search"

    def solve(self) -> None:
        """This method solve the puzzle and save the path to do it.

        It return nothing, but fill in self.solution with the good path.
        """
        # initialization of the border
        queue: list = [[self.heuristic.compute(self.puzzle), self.puzzle]]
        expanded = []  # list of nodes expanded
        self.expanded_nodes = 0  # counter of expanded nodes
        while queue:
            i = 0
            for j in range(1, len(queue)):
                if queue[i][0] > queue[j][0]:  # minimum
                    i = j
            path = queue[i]
            # deletion of the path to the current node in the border
            queue = queue[:i] + queue[i + 1 :]
            node = path[-1]  # current node (last element of the path)
            if node.is_goal():
                self.solution = path[1:]
                self.complexity_memory = len(queue) + self.expanded_nodes
                return
            expanded.append(node.tiles)
            self.expanded_nodes += 1
            # generation of the sons of the node
            move: Puzzle
            for move in node.get_possible_actions():
                if not ((move.tiles in expanded) or move in [x[-1] for x in queue]):
                    new_path = [self.heuristic.compute(move)] + path[1:] + [move]
                    queue.append(new_path)
                # check if node is already in the border
                elif move in [x[-1] for x in queue]:
                    ind = [x[-1] for x in queue].index(move)
                    # we remplace it if it has a better cost
                    if queue[ind][0] > self.heuristic.compute(move):
                        queue.pop(ind)
                        queue.append(path + [move])
