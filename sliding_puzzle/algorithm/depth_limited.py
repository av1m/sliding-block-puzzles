# coding: utf-8

from sliding_puzzle.algorithm.search import Search


class DepthLimited(Search):
    def __repr__(self):
        return "Breadth-Limited Search"

    def solve(self) -> None:
        queue = [[self.puzzle]]
        expanded = []
        self.expanded_nodes = 0
        path = []
        limit = 3
        cutoff = False
        while queue:
            path = queue.pop()
            if path.len() > limit:
                cutoff = True
                continue
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
        if cutoff:
            print("Peut être une solution")
        self.solution = path