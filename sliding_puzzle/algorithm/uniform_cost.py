# coding: utf-8
from typing import List, Union

from sliding_puzzle import Puzzle
from sliding_puzzle.algorithm import Search


class UniformCost(Search):
    def __repr__(self):
        return "Uniform-Cost Search"

    def solve(self) -> None:
        queue = [[self.puzzle]]
        expanded = []
        self.expanded_nodes = 0
        path = []
        while queue:
            cost_min: List[Union[Puzzle, int]] = Search.get_min_cost(queue)
            node: Puzzle = cost_min[0]
            index: int = cost_min[1]
            path = queue.pop(index)
            if node.tiles in expanded:
                continue
            for move in node.get_possible_actions():
                if move.tiles in expanded:
                    continue
                queue.append(path + [move])
            expanded.append([node.tiles, node.cost])
            self.expanded_nodes += 1
            if node.is_goal():
                break
        self.solution = path
