# coding: utf-8
from typing import List

from sliding_puzzle import Puzzle, HeuristicLinearConflicts, Heuristic
from sliding_puzzle.algorithm.search import Search


class GreedyBestFirst(Search):
    def __init__(
        self, init_puzzle: Puzzle, heuristic: Heuristic = HeuristicLinearConflicts
    ):
        super().__init__(init_puzzle)
        self.heuristic = heuristic

    def __str__(self):
        return "Greedy Best-First Search"

    def solve(self) -> None:
        queue: List = [[self.heuristic.compute(self.puzzle), self.puzzle]]
        expanded = []
        self.expanded_nodes = 0
        path = []
        while queue:
            i = 0
            for j in range(1, len(queue)):
                if queue[i][0] > queue[j][0]:  # minimum
                    i = j
            path = queue[i]
            queue = queue[:i] + queue[i + 1 :]
            node = path[-1]
            if node.is_goal():
                self.solution = path[1:]
                return
            expanded.append(node.tiles)
            self.expanded_nodes += 1
            move: Puzzle
            for move in node.get_possible_actions():
                if not ((move.tiles in expanded) or move in [x[-1] for x in queue]):
                    new_path = [self.heuristic.compute(move)] + path[1:] + [move]
                    queue.append(new_path)
                elif move in [x[-1] for x in queue]:
                    ind = [x[-1] for x in queue].index(move)
                    if queue[ind][0] > self.heuristic.compute(move):
                        queue.pop(ind)
                        queue.append(path + [move])
