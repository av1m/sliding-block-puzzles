# coding: utf-8

from __future__ import annotations

from sliding_puzzle import TypePuzzle, Puzzle
from sliding_puzzle.algorithm import Search


class DepthFirst(Search):
    """
    This class implement the interface Search with the Depth First Graph Search algorithm (and no Tree Search).
    """

    def __repr__(self) -> str:
        return "Depth-First Search"

    def solve(self) -> None:
        """
        This method solve the puzzle and save the path to do it.
        It return nothing, but fill in self.solution with the good path.
        """
        queue: list[list[Puzzle]] = [[self.puzzle]]  # initialization of the border
        expanded: list[TypePuzzle] = []  # list of nodes expanded
        self.expanded_nodes = 0  # counter of expanded nodes
        while queue:
            # deletion of the path to the current node in the border
            path: list = queue.pop()
            node: Puzzle = path[-1]  # current node (last element of the path)
            if node.is_goal():
                self.solution = path
                self.complexity_memory = len(queue) + self.expanded_nodes
                return
            expanded.append(node.tiles)
            self.expanded_nodes += 1
            move: Puzzle
            for (
                move
            ) in node.get_possible_actions():  # generation of the sons of the node
                if not ((move.tiles in expanded) or move in [x[-1] for x in queue]):
                    queue.append(path + [move])
