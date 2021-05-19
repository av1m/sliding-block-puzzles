# coding: utf-8
from sliding_puzzle.algorithm import Search


class DepthFirst(Search):
    def __repr__(self):
        return "Depth-First Search"

    def solve(self) -> None:
        queue = [[self.puzzle]]
        expanded = []
        self.expanded_nodes = 0
        while queue:
            path = queue.pop()
            node = path[-1]
            if node.is_goal():
                self.solution = path
                return
            expanded.append(node.tiles)
            self.expanded_nodes += 1
            for move in node.get_possible_actions():
                if not ((move.tiles in expanded) or move in [x[-1] for x in queue]):
                    queue.append(path + [move])
