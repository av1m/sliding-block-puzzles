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
            if node.is_goal():
                self.solution = path
                return
            expanded.append(node.tiles)
            self.expanded_nodes += 1
            for move in node.get_possible_actions():
                if not ((move.tiles in expanded) or move in [x[-1] for x in queue]):
                    queue.append(path + [move])
                elif move in [x[-1] for x in queue]:
                    ind = [x[-1] for x in queue].index(move)
                    if queue[ind][-1].cost > move.cost:
                        queue.pop(ind)
                        queue.append(path + [move])
