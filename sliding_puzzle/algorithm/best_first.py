# -*- coding: utf-8 -*-

from __future__ import annotations

from abc import ABC, abstractmethod

from sliding_puzzle import Puzzle, Heuristic, HeuristicLinearConflicts, TypePuzzle
from sliding_puzzle.algorithm.search import Search


class BestFirst(Search, ABC):
    """
    Interface search for Best First Algorithm

    Children of this class must implemented get_new_path which corresponds to the cost function f (n)
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
        return "Best First Search"

    @abstractmethod
    def get_new_path(self, move: Puzzle, path):
        """Define the function f(n) used for the implementation of a Best First algorithm

        :param move: a child of the puzzle on which we want to have its function f (n)
        :type move: Puzzle
        :param path: Path to reach this Puzzle
        :return: the new path according to the function f(n)
        """
        return

    def solve(self) -> None:
        """This method solve the puzzle and save the path to do it

        This is the standard implementation for any Best First type algorithm.
        The only element that differs is the evaluation of the function of cost f(n),
        which is the subject of a separate method.
        It return nothing, but fill in self.solution (herited from Search class) with the good path.
        """
        # initialization of the border
        queue: list = [[self.heuristic.compute(self.puzzle), self.puzzle]]
        expanded: list[TypePuzzle] = []  # list of nodes expanded
        self.expanded_nodes = 0  # counter of expanded nodes
        while queue:
            i: int = 0
            for j in range(1, len(queue)):
                if queue[i][0] > queue[j][0]:  # minimum
                    i = j
            path = queue[i]
            # deletion of the path to the current node in the border
            queue = queue[:i] + queue[i + 1 :]
            node: Puzzle = path[-1]  # current node (last element of the path)
            if node.is_goal():
                self.solution = path[1:]
                self.complexity_memory = len(queue) + self.expanded_nodes
                return
            expanded.append(node.tiles)
            self.expanded_nodes += 1
            # generation of the sons of the node
            move: Puzzle
            for move in node.get_possible_actions():
                if not ((move.tiles in expanded) or move in [x[-1] for x in queue]):
                    new_path = self.get_new_path(move=move, path=path)
                    queue.append(new_path)
                # check if node is already in the border
                elif move in [x[-1] for x in queue]:
                    ind = [x[-1] for x in queue].index(move)
                    # we replace it if it has a better cost
                    if queue[ind][0] > self.heuristic.compute(move):
                        queue.pop(ind)
                        queue.append(path + [move])
