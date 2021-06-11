# -*- coding: utf-8 -*-

import unittest

from sliding_puzzle.algorithm import *
from sliding_puzzle.representation.puzzle import Puzzle


class UniformCostTestCase(unittest.TestCase):
    def test_UniformCost(self):
        puzzle: Puzzle = Puzzle(
            [[4, 1, 2, 3], [5, 6, 7, 11], [8, 9, 10, 15], [12, 13, 14, 0]]
        )
        strategy = UniformCost(puzzle)
        strategy.solve()
        solution = [x.tiles for x in strategy.solution]
        self.assertEqual(
            [
                [[4, 1, 2, 3], [5, 6, 7, 11], [8, 9, 10, 15], [12, 13, 14, 0]],
                [[4, 1, 2, 3], [5, 6, 7, 11], [8, 9, 10, 0], [12, 13, 14, 15]],
                [[4, 1, 2, 3], [5, 6, 7, 0], [8, 9, 10, 11], [12, 13, 14, 15]],
                [[4, 1, 2, 3], [5, 6, 0, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
                [[4, 1, 2, 3], [5, 0, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
                [[4, 1, 2, 3], [0, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
                [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
            ],
            solution,
        )
        self.assertEqual(241, strategy.expanded_nodes)
