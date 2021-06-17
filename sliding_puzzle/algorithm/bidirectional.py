# -*- coding: utf-8 -*-

from __future__ import annotations

import copy

from sliding_puzzle import Puzzle, Heuristic, HeuristicLinearConflicts
from sliding_puzzle.algorithm import *


class Bidirectional(Search):
    """
    Implementation of the interface Search with the Bidirectionnal algorithm.
    It consist at start a search method on a puzzle and on his goals.
    It's stop when a common puzzle is found.
    """

    def __init__(
        self, init_puzzle: Puzzle, heuristic: Heuristic = HeuristicLinearConflicts
    ) -> None:
        """Initialize the class

        :param init_puzzle: the puzzle we want to solve.
        :type init_puzzle : Puzzle
        :param heuristic: the heuristic we want to use to solve the puzzle
        :type heuristic : Heuristic
        """
        super().__init__(init_puzzle)
        self.heuristic: Heuristic = heuristic

    def __repr__(self) -> str:
        return "Bidirectional search"

    def solve(self) -> None:
        """This method solve the puzzle and save the path to do it.

        It return nothing, but fill in self.solution with the good path.
        """
        # check if the puzzle is already solved
        if self.puzzle.is_goal():
            self.solution = [self.puzzle]
            return

        # creation of the back puzzle
        puzzle2: Puzzle = copy.copy(self.puzzle)
        puzzle2.tiles = copy.deepcopy(self.puzzle.GOAL_STATE)
        puzzle2.GOAL_STATE = copy.deepcopy(self.puzzle.tiles)  # type: ignore

        # border of the front puzzle
        queue: list = [[self.heuristic.compute(self.puzzle), self.puzzle]]
        # border of the back puzzle
        queue2: list = [[self.heuristic.compute(puzzle2), puzzle2]]
        expanded: list = []  # list of nodes expanded (front)
        expanded2: list = []  # list of nodes expanded (back)
        self.expanded_nodes = 0  # counter of expanded nodes

        while queue:
            # Front
            i = 0
            for j in range(1, len(queue)):
                if queue[i][0] > queue[j][0]:  # minimum
                    i = j
            path = queue[i]
            # deletion of the path to the current node in the border
            queue = queue[:i] + queue[i + 1 :]
            node = path[-1]  # current node (last element of the path)

            expanded.append(node.tiles)
            self.expanded_nodes += 1
            # generation of the sons of the node
            move: Puzzle
            for move in node.get_possible_actions():
                # check if the son is in the back border
                if move in [x[-1] for x in queue2]:
                    ind = [x[-1] for x in queue2].index(move)
                    path2 = queue2[ind][1:]
                    path2.reverse()
                    self.solution: list[Puzzle] = path[1:] + path2
                    self.solution[-1].cost = move.cost + path2[0].cost
                    self.complexity_memory = len(queue) + self.expanded_nodes
                    return
                elif not ((move.tiles in expanded) or move in [x[-1] for x in queue]):
                    new_path = (
                        [self.heuristic.compute(move) + move.cost] + path[1:] + [move]
                    )
                    queue.append(new_path)
                # check if node is already in the border
                elif move in [x[-1] for x in queue]:
                    ind = [x[-1] for x in queue].index(move)
                    # we replace it if it has a better cost
                    if queue[ind][0] > self.heuristic.compute(move):
                        queue.pop(ind)
                        queue.append(path + [move])

            # Back
            i = 0
            for j in range(1, len(queue2)):
                if queue2[i][0] > queue2[j][0]:  # minimum
                    i = j
            path2 = queue2[i]
            # deletion of the path to the current node in the border
            queue2 = queue2[:i] + queue2[i + 1 :]
            node2 = path2[-1]  # current node (last element of the path)

            expanded2.append(node2.tiles)
            self.expanded_nodes += 1
            # generation of the sons of the node
            move: Puzzle
            for move in node2.get_possible_actions():
                # check if the son is in the front border
                if move in [x[-1] for x in queue]:
                    ind = [x[-1] for x in queue].index(move)
                    path = queue[ind][1:]
                    path2_middle_end = path2[1:]
                    path2_middle_end.reverse()
                    self.solution = path + path2_middle_end
                    self.solution[-1].cost = move.cost + path[-1].cost
                    self.complexity_memory = len(queue) + self.expanded_nodes
                    return
                elif not ((move.tiles in expanded2) or move in [x[-1] for x in queue2]):
                    new_path = (
                        [self.heuristic.compute(move) + move.cost] + path2[1:] + [move]
                    )
                    queue2.append(new_path)
                # check if node is already in the border
                elif move in [x[-1] for x in queue2]:
                    ind = [x[-1] for x in queue2].index(move)
                    # we replace it if it has a better cost
                    if queue2[ind][0] > self.heuristic.compute(move):
                        queue2.pop(ind)
                        queue2.append(path2 + [move])
