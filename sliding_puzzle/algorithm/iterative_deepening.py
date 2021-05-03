# coding: utf-8

from sliding_puzzle.algorithm import Search


class IterativeDeepening(Search):
    def __repr__(self):
        return "Iterative Deepening Depth-First Search"

    def solve(self) -> None:
        queue2 = [[self.puzzle]]
        expanded = []
        self.expanded_nodes = 0
        path = []
        limit = 3
        while queue2:
            cutoff = False
            queue = queue2.copy()
            while queue:
                path = queue.pop()
                if path.len() > limit:
                    queue2.append(path)
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
            if not cutoff:
                break
            else:
                limit += 3
        self.solution = path
