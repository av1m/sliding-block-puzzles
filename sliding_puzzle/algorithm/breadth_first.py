# coding: utf-8
from sliding_puzzle.algorithm import Search


class BreadthFirst(Search):
    def __repr__(self):
        return "Breadth-First Search"

    def solve(self):
        queue = [[self.puzzle]]
        expanded = []
        self.expanded_nodes = 0
        path = []
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node.tiles in expanded:
                continue
            for move in node.get_possible_actions():
                if move.tiles in expanded:
                    continue
                queue.append(path + [move])
            expanded.append(node.tiles)
            self.expanded_nodes += 1
            if node.is_goal():
                break
        self.solution = path
