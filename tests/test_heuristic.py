# -*- coding: utf-8 -*-

import unittest

from sliding_puzzle import *


class HeuristicTestCase(unittest.TestCase):
    def test_linear_conflicts(self):
        puzzle: Puzzle = Puzzle(
            [[4, 2, 8, 0], [13, 10, 1, 3], [7, 15, 14, 5], [11, 12, 6, 9]]
        )
        self.assertEqual(60, HeuristicLinearConflicts.compute(puzzle))

        puzzle: Puzzle = Puzzle(
            [[4, 2, 8, 0], [13, 10, 1, 3], [7, 15, 14, 5], [11, 12, 6, 9]],
            blank_at_first=False,
        )
        self.assertEqual(62, HeuristicLinearConflicts.compute(puzzle))

    def test_manhattan(self):
        puzzle: Puzzle = Puzzle(
            [[4, 2, 8, 0], [13, 10, 1, 3], [7, 15, 14, 5], [11, 12, 6, 9]]
        )
        self.assertEqual(58, HeuristicManhattan.compute(puzzle))

        puzzle: Puzzle = Puzzle(
            [[4, 2, 8, 0], [13, 10, 1, 3], [7, 15, 14, 5], [11, 12, 6, 9]],
            blank_at_first=False,
        )
        self.assertEqual(60, HeuristicManhattan.compute(puzzle))

    def test_all(self):
        puzzle: Puzzle = Puzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.assertEqual(0, HeuristicLinearConflicts.compute(puzzle))
        self.assertEqual(0, HeuristicManhattan.compute(puzzle))
        puzzle: Puzzle = Puzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]], blank_at_first=False)
        self.assertEqual(18, HeuristicLinearConflicts.compute(puzzle))
        self.assertEqual(18, HeuristicManhattan.compute(puzzle))
        puzzle: Puzzle = Puzzle(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        )
        self.assertEqual(0, HeuristicLinearConflicts.compute(puzzle))
        self.assertEqual(0, HeuristicManhattan.compute(puzzle))
        puzzle: Puzzle = Puzzle(
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
            blank_at_first=False,
        )
        self.assertEqual(32, HeuristicLinearConflicts.compute(puzzle))
        self.assertEqual(32, HeuristicManhattan.compute(puzzle))
        puzzle: Puzzle = Puzzle(
            [
                [1, 2, 3, 4, 5, 6],
                [7, 8, 9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18],
                [19, 20, 21, 22, 23, 24],
                [25, 26, 27, 28, 29, 30],
                [31, 32, 33, 34, 35, 0],
            ]
        )
        self.assertEqual(78, HeuristicLinearConflicts.compute(puzzle))
        self.assertEqual(78, HeuristicManhattan.compute(puzzle))
        puzzle: Puzzle = Puzzle(
            [
                [1, 2, 3, 4, 5, 6],
                [7, 8, 9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18],
                [19, 20, 21, 22, 23, 24],
                [25, 26, 27, 28, 29, 30],
                [31, 32, 33, 34, 35, 0],
            ],
            blank_at_first=False,
        )
        self.assertEqual(0, HeuristicLinearConflicts.compute(puzzle))
        self.assertEqual(0, HeuristicManhattan.compute(puzzle))
        puzzle: Puzzle = Puzzle(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        )
        self.assertEqual(32, HeuristicLinearConflicts.compute(puzzle))
        self.assertEqual(32, HeuristicManhattan.compute(puzzle))
        puzzle: Puzzle = Puzzle(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]],
            blank_at_first=False,
        )
        self.assertEqual(0, HeuristicLinearConflicts.compute(puzzle))
        self.assertEqual(0, HeuristicManhattan.compute(puzzle))
        puzzle: Puzzle = Puzzle(
            [[15, 14, 8, 12], [10, 11, 9, 13], [2, 6, 5, 1], [3, 7, 4, 0]]
        )
        self.assertEqual(89, HeuristicLinearConflicts.compute(puzzle))
        self.assertEqual(89, HeuristicManhattan.compute(puzzle))
        puzzle: Puzzle = Puzzle(
            [[15, 14, 8, 12], [10, 11, 9, 13], [2, 6, 5, 1], [3, 7, 4, 0]],
            blank_at_first=False,
        )
        self.assertEqual(81, HeuristicLinearConflicts.compute(puzzle))
        self.assertEqual(79, HeuristicManhattan.compute(puzzle))
        puzzle: Puzzle = Puzzle([[6, 4, 8], [2, 5, 1], [7, 3, 0]])
        self.assertEqual(20, HeuristicLinearConflicts.compute(puzzle))
        self.assertEqual(20, HeuristicManhattan.compute(puzzle))
        puzzle: Puzzle = Puzzle([[6, 4, 8], [2, 5, 1], [7, 3, 0]], blank_at_first=False)
        self.assertEqual(22, HeuristicLinearConflicts.compute(puzzle))
        self.assertEqual(22, HeuristicManhattan.compute(puzzle))
        puzzle: Puzzle = Puzzle(
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [57, 56, 33, 35, 36, 37, 38, 39, 10],
                [32, 30, 58, 72, 59, 60, 61, 40, 11],
                [31, 55, 34, 74, 76, 80, 62, 41, 12],
                [29, 54, 71, 73, 78, 75, 63, 42, 13],
                [27, 28, 53, 70, 79, 77, 64, 43, 14],
                [0, 52, 69, 68, 67, 66, 65, 44, 15],
                [26, 51, 50, 49, 48, 47, 46, 45, 16],
                [25, 24, 23, 22, 21, 20, 19, 18, 17],
            ]
        )
        self.assertEqual(672, HeuristicLinearConflicts.compute(puzzle))
        self.assertEqual(668, HeuristicManhattan.compute(puzzle))
        puzzle: Puzzle = Puzzle(
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [57, 56, 33, 35, 36, 37, 38, 39, 10],
                [32, 30, 58, 72, 59, 60, 61, 40, 11],
                [31, 55, 34, 74, 76, 80, 62, 41, 12],
                [29, 54, 71, 73, 78, 75, 63, 42, 13],
                [27, 28, 53, 70, 79, 77, 64, 43, 14],
                [0, 52, 69, 68, 67, 66, 65, 44, 15],
                [26, 51, 50, 49, 48, 47, 46, 45, 16],
                [25, 24, 23, 22, 21, 20, 19, 18, 17],
            ],
            blank_at_first=False,
        )
        self.assertEqual(640, HeuristicLinearConflicts.compute(puzzle))
        self.assertEqual(638, HeuristicManhattan.compute(puzzle))
