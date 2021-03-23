# coding: utf-8

from __future__ import annotations

from typing import List, Final

TypePuzzle = List[List[int]]


class Puzzle:
    def __init__(self, tiles: TypePuzzle) -> None:
        if (
            not isinstance(tiles, list)
            or len(tiles) < 0
            or (len(tiles) != len(tiles[0]))
        ):
            raise ValueError("tiles doesn't have the good format")
        # a list of lists representing the puzzle matrix [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.tiles: TypePuzzle = tiles
        self.LEN_TILES: int = len(tiles)
        self.GOAL_STATE: Final[TypePuzzle] = self.goal()

    def __repr__(self) -> str:
        return "Puzzle(n={}, tiles={}, goal={})".format(
            self.LEN_TILES, self.tiles, self.GOAL_STATE
        )

    def __str__(self) -> str:
        return (
            "\n".join(
                ["".join(["{:4}".format(item) for item in row]) for row in self.tiles]
            )
            + "\n"
        )

    def goal(self) -> TypePuzzle:
        """
        Example goal for 4x4 puzzle
        [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        """
        full_tiles_goal = list(range(self.LEN_TILES * self.LEN_TILES))
        parts = self.LEN_TILES
        return [
            full_tiles_goal[
                (i * len(full_tiles_goal))
                // parts : ((i + 1) * len(full_tiles_goal))
                // parts
            ]
            for i in range(parts)
        ]

    def _swap(self, x1, y1, x2, y2) -> TypePuzzle:
        tiles_copy: TypePuzzle = [list(copy_row) for copy_row in self.tiles]
        tiles_copy[x1][y1], tiles_copy[x2][y2] = (
            tiles_copy[x2][y2],
            tiles_copy[x1][y1],
        )

        return tiles_copy

    def _get_coordinates(self, tile: int, tiles: TypePuzzle = None):
        if not tiles:
            tiles = self.tiles

        for i in range(self.LEN_TILES):
            for j in range(self.LEN_TILES):
                if tiles[i][j] == tile:
                    return i, j

        return RuntimeError("Invalid tile value")

    def get_possible_moves(self) -> List[Puzzle]:
        """
        Returns a list of all the possible moves
        """
        moves: List[Puzzle] = []
        i, j = self._get_coordinates(0)  # blank space
        if i > 0:
            moves.append(Puzzle(self._swap(i, j, i - 1, j)))  # move up
        if j < self.LEN_TILES - 1:
            moves.append(Puzzle(self._swap(i, j, i, j + 1)))  # move right
        if j > 0:
            moves.append(Puzzle(self._swap(i, j, i, j - 1)))  # move left
        if i < self.LEN_TILES - 1:
            moves.append(Puzzle(self._swap(i, j, i + 1, j)))  # move down
        return moves

    def heuristic_misplaced(self) -> float:
        """
        Counts the number of misplaced tiles
        """
        return sum(
            1
            for i in range(self.LEN_TILES)
            for j in range(self.LEN_TILES)
            if self.tiles[i][j] != self.GOAL_STATE[i][j]
        )

    def heuristic_manhattan_distance(self) -> float:
        """
        Counts how much is a tile misplaced from the original position
        """

        def _get_distance(i, j):
            i1, j1 = self._get_coordinates(self.tiles[i][j], self.GOAL_STATE)
            return abs(i - i1) + abs(j - j1)

        return sum(
            _get_distance(i, j)
            for i in range(self.LEN_TILES)
            for j in range(self.LEN_TILES)
        )
