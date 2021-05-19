# coding: utf-8
from typing import List

from sliding_puzzle.algorithm import Search


class BreadthFirst(Search):
    def __repr__(self):
        return "Breadth-First Search"

    def solve(self):
        queue: List = [[self.puzzle]]
        self.expanded_nodes = 0
        if self.puzzle.is_goal():
            self.solution = queue[-1]
            return
        expanded = []
        while queue:
            path = queue.pop(0)
            node = path[-1]
            expanded.append(node.tiles)
            self.expanded_nodes += 1
            for move in node.get_possible_actions():
                if not ((move.tiles in expanded) or move in [x[-1] for x in queue]):
                    queue.append(path + [move])
                    if move.is_goal():
                        self.solution = queue[-1]
                        return
        assert not self.solution  # no solution
