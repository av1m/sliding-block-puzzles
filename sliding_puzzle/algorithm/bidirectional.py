# coding: utf-8
import copy
from typing import List

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
    ):
        """Initialize the class
        :param init_puzzle: the puzzle we want to solve.
        :type init_puzzle : Puzzle
        :param heuristic: the heuristic we want to use to solve the puzzle
        :type heuristic : Heuristic
        """
        super().__init__(init_puzzle)
        self.heuristic = heuristic

    def __str__(self):
        return "Bidirectionnal"

    def solve(self) -> None:
        """
        This method solve the puzzle and save the path to do it.
        It return nothing, but fill in self.solution with the good path.
        """
        # creation of the back puzzle
        puzzle2 = copy.deepcopy(self.puzzle)
        puzzle2.tiles = copy.deepcopy(self.puzzle.GOAL_STATE)
        puzzle2.GOAL_STATE = copy.deepcopy(self.puzzle.tiles)

        queue: List = [
            [self.heuristic.compute(self.puzzle), self.puzzle]
        ]  # border of the front puzzle
        queue2: List = [
            [self.heuristic.compute(puzzle2), puzzle2]
        ]  # border of the back puzzle
        expanded: List = []  # list of nodes expanded (front)
        expanded2: List = []  # list of nodes expanded (back)
        self.expanded_nodes = 0  # counter of expanded nodes

        while queue:
            # Front
            i = 0
            for j in range(1, len(queue)):
                if queue[i][0] > queue[j][0]:  # minimum
                    i = j
            path = queue[i]
            queue = (
                queue[:i] + queue[i + 1 :]
            )  # deletion of the path to the current node in the border
            node = path[-1]  # current node (last element of the path)

            expanded.append(node.tiles)
            self.expanded_nodes += 1
            for (
                move
            ) in node.get_possible_actions():  # generation of the sons of the node
                if move in [
                    x[-1] for x in queue2
                ]:  # check if the son is in the back border
                    ind = [x[-1] for x in queue2].index(move)
                    path2 = queue2[ind][1:]
                    path2.reverse()
                    self.solution = path[1:] + path2
                    self.complexity_memory = len(queue) + self.expanded_nodes
                    return
                elif not ((move.tiles in expanded) or move in [x[-1] for x in queue]):
                    new_path = (
                        [self.heuristic.compute(move) + move.cost] + path[1:] + [move]
                    )
                    queue.append(new_path)
                elif move in [
                    x[-1] for x in queue
                ]:  # check if node is already in the border
                    ind = [x[-1] for x in queue].index(move)
                    if queue[ind][0] > self.heuristic.compute(
                        move
                    ):  # we replace it if it has a better cost
                        queue.pop(ind)
                        queue.append(path + [move])

            # Back
            i = 0
            for j in range(1, len(queue2)):
                if queue2[i][0] > queue2[j][0]:  # minimum
                    i = j
            path2 = queue2[i]
            queue2 = (
                queue2[:i] + queue2[i + 1 :]
            )  # deletion of the path to the current node in the border
            node2 = path2[-1]  # current node (last element of the path)

            expanded2.append(node2.tiles)
            self.expanded_nodes += 1
            for (
                move
            ) in node2.get_possible_actions():  # generation of the sons of the node
                if move in [
                    x[-1] for x in queue
                ]:  # check if the son is in the front border
                    ind = [x[-1] for x in queue].index(move)
                    path = queue[ind][1:]
                    path2 = path2[1:]
                    path2.reverse()
                    self.solution = path + path2
                    self.complexity_memory = len(queue) + self.expanded_nodes
                    return
                elif not ((move.tiles in expanded2) or move in [x[-1] for x in queue2]):
                    new_path = (
                        [self.heuristic.compute(move) + move.cost] + path2[1:] + [move]
                    )
                    queue2.append(new_path)
                elif move in [
                    x[-1] for x in queue2
                ]:  # check if node is already in the border
                    ind = [x[-1] for x in queue2].index(move)
                    if queue2[ind][0] > self.heuristic.compute(
                        move
                    ):  # we replace it if it has a better cost
                        queue2.pop(ind)
                        queue2.append(path2 + [move])
