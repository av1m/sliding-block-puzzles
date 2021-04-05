from algorithm.search import Search


class BreadthFirst(Search):
    def __init__(self, initial_puzzle):
        super().__init__(initial_puzzle)
        self.start = initial_puzzle

    def solve(self):
        queue = [[self.start]]
        expanded = []
        self.expanded_nodes = 0
        path = []
        while queue:
            path = queue.pop(0)
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
