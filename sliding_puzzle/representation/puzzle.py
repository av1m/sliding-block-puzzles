# coding: utf-8

from __future__ import annotations

import copy
import logging
from typing import List, Final, Tuple

logger = logging.getLogger(__name__)

TypePuzzle = List[List[int]]


class Puzzle:
    def __init__(self, tiles: TypePuzzle, cost: int = 0) -> None:
        self.check_tiles(tiles)
        # a list of lists representing the puzzle matrix [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.tiles: TypePuzzle = tiles
        self.LEN_TILES: Final[int] = len(tiles)
        self.GOAL_STATE: Final[TypePuzzle] = self._goal()
        self.BLANK: Final[int] = 0
        # cout de deplacement pour aller du puzzle initial au puzzle en cours
        self.cost: int = cost

    def __repr__(self) -> str:
        return "Puzzle(n={}, tiles={}, goal={}, cost={})".format(
            self.LEN_TILES, self.tiles, self.GOAL_STATE, self.cost
        )

    def __str__(self) -> str:
        return (
            "\n".join(
                ["".join(["{:4}".format(item) for item in row]) for row in self.tiles]
            )
            + "\n"
        )

    def _goal(self) -> TypePuzzle:
        """
        Example goal for 4x4 puzzle
        [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        """
        full_tiles_goal = list(range(self.LEN_TILES ** 2))
        return [
            full_tiles_goal[x : x + self.LEN_TILES]
            for x in range(0, len(full_tiles_goal), self.LEN_TILES)
        ]

    def _transition(
        self, ii: Tuple[int] or List[int], jj: Tuple[int] or List[int]
    ) -> TypePuzzle:
        """https://stackoverflow.com/a/2493980 """
        tiles = copy.deepcopy(self.tiles)
        tiles[ii[0]][ii[1]], tiles[jj[0]][jj[1]] = (
            tiles[jj[0]][jj[1]],
            tiles[ii[0]][ii[1]],
        )
        return tiles

    def get_index(self, tile: int, tiles: TypePuzzle = None):
        """
        return row, col (index) need + 1
        :param tile:
        :param tiles:
        :return:
        """
        tiles = tiles if tiles else self.tiles
        tile_index = [item for sublist in tiles for item in sublist].index(tile)
        return tile_index // self.LEN_TILES, tile_index % self.LEN_TILES

    def get_possible_actions(self) -> List[Puzzle]:
        """
        :return: All possible moves
        """
        moves: List[Puzzle] = []
        i, j = self.get_index(self.BLANK)

        def add_action(ij_new) -> None:
            tiles_: Puzzle = Puzzle(self._transition((i, j), ij_new))
            tiles_.cost = tiles_.get_cost(ij_new[0], ij_new[1])
            moves.append(tiles_)

        if i > 0:  # up
            add_action((i - 1, j))
        if j < self.LEN_TILES - 1:  # right
            add_action((i, j + 1))
        if j > 0:  # left
            add_action((i, j - 1))
        if i < self.LEN_TILES - 1:  # down
            add_action((i + 1, j))
        return moves

    def get_cost(self, i, j) -> int:
        return self.cost + (1 if self.tiles[i][j] % 2 == 0 else 2)

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
            i1, j1 = self.get_index(self.tiles[i][j], self.GOAL_STATE)
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

    def __lt__(self, other: Puzzle) -> bool:
        return self.cost < other.cost

    def is_goal(self) -> bool:
        return self.tiles == self.GOAL_STATE

    @staticmethod
    def puzzles_to_list(list_puzzle: List[Puzzle]) -> List[TypePuzzle]:
        return [x.tiles for x in list_puzzle]

    @staticmethod
    def check_tiles(tiles: TypePuzzle) -> None:
        """
        Check if the tiles passed as parameters is valid
        :param tiles: a list of lists representing the puzzle matrix. For Example [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        :return: True if valid else otherwise
        """
        if (
            not isinstance(tiles, list)
            or len(tiles) < 0
            or (len(tiles) != len(tiles[0]))
        ):
            raise ValueError("tiles {0} doesn't have the good format".format(tiles))
        flat_tiles = sorted([item for sublist in tiles for item in sublist])
        ordered_tiles = list(range(len(tiles) ** 2))
        if not flat_tiles == ordered_tiles:
            raise ValueError(
                "Don't match pattern. Expected {0}, actual {1}".format(
                    ordered_tiles, flat_tiles
                )
            )
