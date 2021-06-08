# coding: utf-8
from sliding_puzzle.algorithm import Search


class DepthFirst(Search):
    """
    This class implement the interface Search with the Depth First Graph Search algorithm (and no Tree Search).
    """

    def __repr__(self):
        return "Depth-First Search"

    def solve(self) -> None:
        """
        This method solve the puzzle and save the path to do it.
        It return nothing, but fill in self.solution with the good path.
        """
        queue = [[self.puzzle]]  # initialization of the border
        expanded = []  # list of nodes expanded
        self.expanded_nodes = 0  # counter of expanded nodes
        while queue:
            path = queue.pop()  # deletion of the path to the current node in the border
            node = path[-1]  # current node (last element of the path)
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
