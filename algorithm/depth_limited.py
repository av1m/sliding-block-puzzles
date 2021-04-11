# coding: utf-8

from algorithm.search import Search


class DepthLimited(Search):
    def __repr__(self):
        return "Breadth-Limited Search"

    def solve(self) -> None:
        queue = [[self.puzzle]]
        expanded = []
        self.expanded_nodes = 0
        path = []
        limit = 3
        while queue:
            path = queue.pop()
            node = path[-1]
            if node.tiles in expanded:
                continue
            for move in node.get_possible_moves():
                if move.tiles in expanded:
                    continue
                queue.append(path + [move])
            expanded.append(node.tiles)
            self.expanded_nodes += 1
            if node.is_goal():
                break
        self.solution = path
