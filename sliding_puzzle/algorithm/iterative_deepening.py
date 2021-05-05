# coding: utf-8

from sliding_puzzle.algorithm import Search


class IterativeDeepening(Search):
    def __repr__(self):
        return "Iterative Deepening Depth-First Search"

    def solve(self) -> None:
        queue = [[self.puzzle]]
        expanded = []
        self.expanded_nodes = 0
        path = []
        limit = 3
        solution = False
        while queue:
            queue2 = queue.copy()
            queue = []
            while queue2:
                path = queue2.pop()
                if len(path) > limit:
                    queue.append(path)
                    continue
                node = path[-1]
                if node.tiles in expanded:
                    continue
                for move in node.get_possible_actions():
                    if move.tiles in expanded:
                        continue
                    queue2.append(path + [move])
                expanded.append(node.tiles)
                self.expanded_nodes += 1
                if node.is_goal():
                    solution = True
                    break
            if solution:
                break
            else:
                limit += 3
        self.solution = path
