# coding: utf-8

from __future__ import annotations

import copy
import logging
from typing import List, Final, Tuple

logger = logging.getLogger(__name__)

TypePuzzle = List[List[int]]


def return_puzzle(is_list: bool = False):
    def decorator(function):
        def wrapper(*args, **kwargs):
            func = function(*args, **kwargs)
            if kwargs.get("return_puzzle"):
                if is_list:
                    return [Puzzle(tiles) for tiles in func]
                return Puzzle(func)
            return func

        return wrapper

    return decorator


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
        self.LEN_TILES: Final[int] = len(tiles)
        self.GOAL_STATE: Final[TypePuzzle] = self.goal()
        self.BLANK: Final[int] = 0

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
        return [
            full_tiles_goal[
                (i * len(full_tiles_goal))
                // self.LEN_TILES : ((i + 1) * len(full_tiles_goal))
                // self.LEN_TILES
            ]
            for i in range(self.LEN_TILES)
        ]

    @return_puzzle()
    def _swap(
        self, ii: Tuple[int] or List[int], jj: Tuple[int] or List[int], **kwargs
    ) -> TypePuzzle or Puzzle:
        """https://stackoverflow.com/a/2493980 """
        tiles = copy.deepcopy(self.tiles)
        tiles[ii[0]][ii[1]], tiles[jj[0]][jj[1]] = (
            tiles[jj[0]][jj[1]],
            tiles[ii[0]][ii[1]],
        )
        return tiles

    def _get_index(self, tile: int, tiles: TypePuzzle = None):
        tiles = tiles if tiles else self.tiles
        tile_index = [item for sublist in tiles for item in sublist].index(tile)
        return tile_index // self.LEN_TILES, tile_index % self.LEN_TILES

    @return_puzzle(is_list=True)
    def get_possible_moves(
        self, return_puzzle: bool = False, **kwargs
    ) -> List[TypePuzzle] or List[Puzzle]:
        """
        :return: All possible moves
        """
        moves: List[TypePuzzle] or List[Puzzle] = []
        i, j = self._get_index(self.BLANK)
        add_moves = lambda jj: moves.append(self._swap((i, j), jj))
        if i > 0:  # up
            add_moves((i - 1, j))
        if j < self.LEN_TILES - 1:  # right
            add_moves((i, j + 1))
        if j > 0:  # left
            add_moves((i, j - 1))
        if i < self.LEN_TILES - 1:  # down
            add_moves((i + 1, j))
        return moves

    def get_cost(self, i, j):
        return 1 if self.tiles[i][j] % 2 == 0 else 2

    def heuristic_misplaced(self) -> float:
        """
        Counts the number of misplaced tiles
        """
        return sum(
            self.get_cost(i, j)
            for i in range(self.LEN_TILES)
            for j in range(self.LEN_TILES)
            if self.tiles[i][j] != self.GOAL_STATE[i][j]
        )

    def heuristic_manhattan_distance(self) -> float:
        """
        Counts how much is a tile misplaced from the original position
        """

        def _get_distance(i, j):
            i1, j1 = self._get_index(self.tiles[i][j], self.GOAL_STATE)
            return abs(i - i1) + abs(j - j1)

        return sum(
            _get_distance(i, j)
            for i in range(self.LEN_TILES)
            for j in range(self.LEN_TILES)
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Puzzle):
            logger.warning(
                "{} isn't type 'Puzzle'. So, will use default __eq__".format(
                    type(o).__name__
                )
            )
            return super().__eq__(o)
        return self.tiles == o.tiles

    def is_goal(self):
        return self.tiles == self.GOAL_STATE
