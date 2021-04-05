# coding: utf-8

from algorithm.search import Search
from typing import List
from representation.puzzle import Puzzle


class UniformCost(Search):
    def __init__(self, init_puzzle: Puzzle):
        super().__init__(init_puzzle)

    def solve(self) -> None:
        if self.puzzle.is_goal():
            return
        path = []
        queue: List = [[self.puzzle.heuristic_manhattan_distance(), self.puzzle, path]]
        expanded: List = []
        while queue:
            i = 0
            for j in range(1, len(queue)):
                if queue[i][0] > queue[j][0]:  # minimum
                    i = j

            node = queue[i]
            queue = queue[:i] + queue[i + 1 :]
            expanded.append(node[1])
            if node.is_goal():
                self.solution = node[0] + node[1]
                self.expanded_nodes = len(expanded)
                return
            for action in node.get_possible_moves:
                child = action
                path2 = node[0] + node[1]
                if child not in expanded and child not in queue[:][1]:
                    queue.append([child.heuristic_manhattan_distance(), child, path2])
                elif child in queue[:][1]:
                    if (
                        queue[queue[:][1].index(child)][0]
                        > child.heuristic_manhattan_distance()
                    ):
                        queue[queue[:][1].index(child)] = [
                            child.heuristic_manhattan_distance(),
                            child,
                            path2,
                        ]
