# coding: utf-8
import unittest

from sliding_puzzle.algorithm.search import Search
from sliding_puzzle.representation.puzzle import Puzzle


class SearchTestCase(unittest.TestCase):
    def test_is_solvable_8(self):
        solvable = [
            [[0, 1, 2], [4, 5, 3], [7, 8, 6]],
            [[1, 2, 3], [0, 4, 6], [7, 5, 8]],
            [[1, 0, 3], [7, 2, 5], [8, 4, 6]],
        ]

        not_solvable = [
            [[1, 2, 3], [6, 8, 4], [5, 7, 0]],
            [[1, 2, 3], [4, 5, 6], [8, 7, 0]],
            [[1, 5, 0], [3, 2, 8], [4, 6, 7]],
        ]

        [self.assertTrue(Search.is_solvable(Puzzle(p))) for p in solvable]
        [self.assertFalse(Search.is_solvable(Puzzle(p))) for p in not_solvable]

    def test_is_solvable_15(self):
        solvable = [
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12], [13, 14, 15, 11]],
            [[4, 1, 2, 3], [5, 6, 7, 11], [8, 9, 10, 15], [12, 13, 14, 0]],
        ]
        not_solvable = [
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]],
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 11], [13, 14, 15, 12]],
        ]
        [self.assertTrue(Search.is_solvable(Puzzle(p))) for p in solvable]
        [self.assertFalse(Search.is_solvable(Puzzle(p))) for p in not_solvable]
