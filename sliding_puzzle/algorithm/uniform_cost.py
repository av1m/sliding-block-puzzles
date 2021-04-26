# coding: utf-8

from sliding_puzzle.algorithm.search import Search


class UniformCost(Search):
    def __repr__(self):
        return "Uniform-Cost Search"

    def solve(self) -> None:
        queue = [[self.puzzle]]
        expanded = []
        self.expanded_nodes = 0
        path = []
        while queue:
            node, index = Search.get_min_cost(queue)
            path = queue.pop(index)
            if node.tiles in expanded:
                continue
            for move in node.get_possible_moves():
                if move.tiles in expanded:
                    continue
                queue.append(path + [move])
            expanded.append([node.tiles, node.cost])
            self.expanded_nodes += 1
            if node.is_goal():
                break
        self.solution = path
