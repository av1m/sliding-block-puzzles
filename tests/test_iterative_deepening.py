# -*- coding: utf-8 -*-

import unittest

from sliding_puzzle.algorithm import *
from sliding_puzzle.representation.puzzle import Puzzle


class IterativeDeepeningTestCase(unittest.TestCase):
    def test_IterativeDeepening(self):
        puzzle: Puzzle = Puzzle(
            [[1, 2, 3, 7], [4, 5, 6, 11], [8, 9, 10, 15], [12, 13, 14, 0]]
        )
        strategy = IterativeDeepening(puzzle)
        strategy.solve()
        solution = [x.tiles for x in strategy.solution]
        self.assertEqual(
            [
                [[1, 2, 3, 7], [4, 5, 6, 11], [8, 9, 10, 15], [12, 13, 14, 0]],
                [[1, 2, 3, 7], [4, 5, 6, 11], [8, 9, 10, 15], [12, 13, 0, 14]],
                [[1, 2, 3, 7], [4, 5, 6, 11], [8, 9, 10, 15], [12, 13, 14, 0]],
                [[1, 2, 3, 7], [4, 5, 6, 11], [8, 9, 10, 0], [12, 13, 14, 15]],
                [[1, 2, 3, 7], [4, 5, 6, 0], [8, 9, 10, 11], [12, 13, 14, 15]],
                [[1, 2, 3, 0], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
                [[1, 2, 0, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
                [[1, 0, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
                [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
            ],
            solution,
        )
        self.assertEqual(0, strategy.expanded_nodes)
