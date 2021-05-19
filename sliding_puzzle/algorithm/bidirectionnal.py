# coding: utf-8
import copy
from typing import List

from sliding_puzzle import Puzzle, Heuristic, HeuristicManhattan
from sliding_puzzle.algorithm import *


class Bidirectionnal(Search):
    def __init__(self, init_puzzle: Puzzle, heuristic: Heuristic = HeuristicManhattan):
        super().__init__(init_puzzle)
        self.heuristic = heuristic

    def __str__(self):
        return "Bidirectionnal"

    def solve(self) -> None:
        # creation of the back puzzle
        puzzle2 = copy.deepcopy(self.puzzle)
        puzzle2.tiles = copy.deepcopy(self.puzzle.GOAL_STATE)
        puzzle2.GOAL_STATE = copy.deepcopy(self.puzzle.tiles)

        queue: List = [[self.heuristic.compute(self.puzzle), self.puzzle]]
        queue2: List = [[self.heuristic.compute(puzzle2), puzzle2]]
        expanded: List = []
        expanded2: List = []
        self.expanded_nodes = 0

        while queue:
            # Front
            i = 0
            for j in range(1, len(queue)):
                if queue[i][0] > queue[j][0]:  # minimum
                    i = j
            path = queue[i]
            queue = queue[:i] + queue[i + 1 :]
            node = path[-1]

            # Front
            expanded.append(node.tiles)
            self.expanded_nodes += 1
            for move in node.get_possible_actions():
                if move in [x[-1] for x in queue2]:
                    ind = [x[-1] for x in queue2].index(move)
                    path2 = queue2[ind][1:]
                    path2.reverse()
                    self.solution = path[1:] + path2
                    return
                elif not ((move.tiles in expanded) or move in [x[-1] for x in queue]):
                    new_path = (
                        [self.heuristic.compute(move) + move.cost] + path[1:] + [move]
                    )
                    queue.append(new_path)
                elif move in [x[-1] for x in queue]:
                    ind = [x[-1] for x in queue].index(move)
                    if queue[ind][0] > self.heuristic.compute(move):
                        queue.pop(ind)
                        queue.append(path + [move])

            # Back
            i = 0
            for j in range(1, len(queue2)):
                if queue2[i][0] > queue2[j][0]:  # minimum
                    i = j
            path2 = queue2[i]
            queue2 = queue2[:i] + queue2[i + 1 :]
            node2 = path2[-1]

            expanded2.append(node2.tiles)
            self.expanded_nodes += 1
            for move in node2.get_possible_actions():
                if move in [x[-1] for x in queue]:
                    ind = [x[-1] for x in queue].index(move)
                    path = queue[ind][1:]
                    path2 = path2[1:]
                    path2.reverse()
                    self.solution = path + path2
                    return
                elif not ((move.tiles in expanded2) or move in [x[-1] for x in queue2]):
                    new_path = (
                        [self.heuristic.compute(move) + move.cost] + path2[1:] + [move]
                    )
                    queue2.append(new_path)
                elif move in [x[-1] for x in queue2]:
                    ind = [x[-1] for x in queue2].index(move)
                    if queue2[ind][0] > self.heuristic.compute(move):
                        queue2.pop(ind)
                        queue2.append(path2 + [move])
