# -*- coding: utf-8 -*-

from __future__ import annotations

from sliding_puzzle import Puzzle, TypePuzzle
from sliding_puzzle.algorithm import Search


class BreadthFirst(Search):
    """
    Implementation of the interface Search with the Breadth First algorithm.
    """

    def __repr__(self) -> str:
        return "Breadth-First Search"

    def solve(self) -> None:
        """This method solve the puzzle and save the path to do it.

        It return nothing, but fill in self.solution with the good path.
        """
        queue: list[list[Puzzle]] = [[self.puzzle]]  # initialization of the border
        self.expanded_nodes: int = 0  # counter of expanded nodes
        if self.puzzle.is_goal():
            self.solution = queue[-1]
            return
        expanded: list[TypePuzzle] = []  # list of nodes expanded
        while queue:
            path: list = queue.pop(0)  # deletion of current node in the border
            node: Puzzle = path[-1]
            expanded.append(node.tiles)
            self.expanded_nodes += 1
            move: Puzzle
            for (
                move
            ) in node.get_possible_actions():  # generation of the sons of the node
                if not ((move.tiles in expanded) or move in [x[-1] for x in queue]):
                    queue.append(path + [move])
                    if move.is_goal():
                        self.solution = queue[-1]
                        self.complexity_memory = len(queue) + self.expanded_nodes
                        return
        assert not self.solution  # no solution
