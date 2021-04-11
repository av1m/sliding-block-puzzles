# coding: utf-8

import unittest
from typing import List

from representation.puzzle import Puzzle, TypePuzzle


class PuzzleTestCase(unittest.TestCase):
    def test_index3(self):
        puzzle: Puzzle = Puzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        self.assertEqual((2, 1), puzzle._get_index(0))
        self.assertEqual((0, 0), puzzle._get_index(1))
        self.assertEqual((2, 2), puzzle._get_index(8))
        self.assertEqual((1, 1), puzzle._get_index(5))

    def test_index4(self):
        puzzle: Puzzle = Puzzle(
            [[4, 1, 2, 3], [5, 6, 7, 11], [8, 9, 10, 15], [12, 13, 14, 0]]
        )
        self.assertEqual((3, 3), puzzle._get_index(0))
        self.assertEqual((0, 1), puzzle._get_index(1))
        self.assertEqual((2, 0), puzzle._get_index(8))
        self.assertEqual((1, 0), puzzle._get_index(5))

    def test_swap3(self):
        puzzle: Puzzle = Puzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        self.assertEqual(
            [[5, 2, 3], [4, 1, 6], [7, 0, 8]], puzzle._swap((0, 0), (1, 1))
        )
        self.assertEqual(
            [[1, 2, 3], [0, 5, 6], [7, 4, 8]], puzzle._swap((2, 1), (1, 0))
        )

    def test_possible_moves3(self):
        puzzle: Puzzle = Puzzle([[4, 5, 3], [1, 2, 8], [7, 0, 6]])
        moves: List[Puzzle] = [
            Puzzle([[4, 5, 3], [1, 2, 8], [7, 6, 0]]),  # right
            Puzzle([[4, 5, 3], [1, 0, 8], [7, 2, 6]]),  # up
            Puzzle([[4, 5, 3], [1, 2, 8], [0, 7, 6]]),  # left
        ]
        self.assertTrue(all(x in puzzle.get_possible_moves() for x in moves))

        moves: List[TypePuzzle] = [
            [[4, 5, 3], [1, 2, 8], [7, 6, 0]],  # right
            [[4, 5, 3], [1, 0, 8], [7, 2, 6]],  # up
            [[4, 5, 3], [1, 2, 8], [0, 7, 6]],  # left
        ]
        self.assertTrue(
            all(x in Puzzle.puzzles_to_list(puzzle.get_possible_moves()) for x in moves)
        )

    def test_possible_moves4(self):
        puzzle: Puzzle = Puzzle(
            [[4, 1, 2, 3], [5, 6, 7, 11], [8, 9, 0, 15], [12, 13, 14, 10]]
        )
        moves: List[TypePuzzle] = [
            [[4, 1, 2, 3], [5, 6, 0, 11], [8, 9, 7, 15], [12, 13, 14, 10]],  # up
            [[4, 1, 2, 3], [5, 6, 7, 11], [8, 9, 15, 0], [12, 13, 14, 10]],  # right
            [[4, 1, 2, 3], [5, 6, 7, 11], [8, 0, 9, 15], [12, 13, 14, 10]],  # left
            [[4, 1, 2, 3], [5, 6, 7, 11], [8, 9, 14, 15], [12, 13, 0, 10]],  # down
        ]
        self.assertTrue(
            all(x in Puzzle.puzzles_to_list(puzzle.get_possible_moves()) for x in moves)
        )


if __name__ == "__main__":
    unittest.main()
