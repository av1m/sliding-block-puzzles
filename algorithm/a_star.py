# coding: utf-8
from typing import List

from algorithm.search import Search


class AStar(Search):
    def __str__(self):
        return "A*"

    def solve(self) -> None:
        queue: List = [[self.puzzle.heuristic_manhattan_distance(), self.puzzle]]
        expanded: List = []
        path = None
        self.expanded_nodes = 0

        while queue:
            i = 0
            for j in range(1, len(queue)):
                if queue[i][0] > queue[j][0]:  # minimum
                    i = j

            path = queue[i]
            queue = queue[:i] + queue[i + 1 :]
            node = path[-1]

            if node.is_goal():
                break
            if node.tiles in expanded:
                continue

            for move in node.get_possible_moves(return_puzzle=True):
                if move.tiles in expanded:
                    continue
                new_path = (
                    [
                        path[0]
                        + (
                            move.heuristic_manhattan_distance()
                            - node.heuristic_manhattan_distance()
                        )
                    ]
                    + path[1:]
                    + [move]
                )

                queue.append(new_path)
                expanded.append(node.tiles)

            self.expanded_nodes += 1
        self.solution = path[1:]
