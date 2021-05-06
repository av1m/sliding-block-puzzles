# coding: utf-8
from typing import List

from sliding_puzzle import Puzzle, Heuristic, HeuristicManhattan
from sliding_puzzle.algorithm.search import Search


class AStar(Search):
    def __init__(self, init_puzzle: Puzzle, heuristic: Heuristic = HeuristicManhattan):
        super().__init__(init_puzzle)
        self.heuristic = heuristic

    def __str__(self):
        return "A*"

    def solve(self) -> None:
        queue: List = [[self.heuristic.compute(self.puzzle), self.puzzle]]
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
            node: Puzzle = path[-1]

            if node.is_goal():
                break
            if node.tiles in expanded:
                continue

            move: Puzzle
            for move in node.get_possible_actions():
                if move.tiles in expanded:
                    continue
                new_path = (
                    [
                        path[0]
                        + (
                            self.heuristic.compute(move)
                            - self.heuristic.compute(node)
                            + move.cost
                            - node.cost
                        )
                    ]
                    + path[1:]
                    + [move]
                )

                queue.append(new_path)
                expanded.append(node.tiles)
            self.expanded_nodes += 1
        self.solution = path[1:]
