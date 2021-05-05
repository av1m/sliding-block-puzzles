# coding: utf-8
"""
Representation of a sliding puzzle,
also called sliding block puzzle or sliding tile puzzle
"""

from __future__ import annotations

import copy
import logging
from typing import List, Final, Tuple

logger = logging.getLogger(__name__)

TypePuzzle = List[List[int]]


class Puzzle:
    """Representation of a sliding puzzle, sliding block puzzle, or sliding tile puzzle

    Example::

        puzzle: Puzzle = Puzzle([[3, 1, 2], [0, 4, 5], [6, 7, 8]])
        print(puzzle)
    """

    def __init__(
        self, tiles: TypePuzzle, cost: int = 0, blank_at_first: bool = True
    ) -> None:
        """Constructor method

        :param tiles: A list of lists representing the puzzle matrix [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        :type tiles: TypePuzzle
        :param cost: Indicates in which position the BLANK must be (first or last), defaults to 0
        :type cost: int, optional
        :param blank_at_first: Represents the cost of moving from the initial puzzle to the current puzzle (self),
            defaults to True
        :type blank_at_first: bool, optional
        """
        self._tiles: TypePuzzle = tiles
        self.cost: int = cost
        self.BLANK_AT_FIRST: Final[bool] = blank_at_first
        self.LEN_TILES: Final[int] = len(tiles)
        self.GOAL_STATE: Final[TypePuzzle] = self._goal()
        self.BLANK: Final[int] = 0

    def __repr__(self) -> str:
        """s"""
        return "Puzzle(n={}, tiles={}, goal={}, cost={})".format(
            self.LEN_TILES, self.tiles, self.GOAL_STATE, self.cost
        )

    def __str__(self) -> str:
        """s"""
        return (
            "\n".join(
                ["".join(["{:4}".format(item) for item in row]) for row in self.tiles]
            )
            + "\n"
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

    def __len__(self) -> int:
        """Allows you to know the length of the puzzle.

        For example::

        - len(Puzzle([[4, 1, 2, 3], [5, 6, 7, 11], [8, 9, 10, 15], [12, 13, 14, 0]])) will return 4
        - len(Puzzle([[3, 1, 2], [0, 4, 5], [6, 7, 8]])) will return 3

        :return: the length of the puzzle
        :rtype: int
        """
        return self.LEN_TILES

    @property
    def tiles(self) -> TypePuzzle:
        """Getter of tiles self.check_tiles(tiles)

        :return: The Puzzle in the form of a list
        :rtype: TypePuzzle
        """
        return self._tiles

    @tiles.setter
    def tiles(self, tiles: TypePuzzle) -> None:
        """ Setter of tiles attribute.
        We check that tiles have the correct format
        """
        self.check_tiles(tiles)
        self._tiles = tiles

    def _goal(self) -> TypePuzzle:
        """Determines the final state (goal) of the game

        `sliding_puzzle.representation.puzzle.TypePuzzle`_


        Example::

            For 4x4 puzzle if BLANK_AT_FIRST:
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
            For 3x3 puzzle if not BLANK_AT_FIRST:
            [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

        :return: the final state of the game
        :rtype: TypePuzzle
        """
        full_tiles_goal = list(range(1, self.LEN_TILES ** 2))
        full_tiles_goal.insert(0 if self.BLANK_AT_FIRST else len(full_tiles_goal), 0)
        return [
            full_tiles_goal[x : x + self.LEN_TILES]
            for x in range(0, len(full_tiles_goal), self.LEN_TILES)
        ]

    def _transition(
        self, ii: Tuple[int] or List[int], jj: Tuple[int] or List[int]
    ) -> TypePuzzle:
        """Transitions a tile

        `Inspired by this answer <https://stackoverflow.com/a/2493980>`_

        Allows you to change two elements together, for example::

            Our puzzle
            [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
            And we call self._transition((1, 1), (2,2))
            [[1, 2, 3], [4, 0, 6], [7, 8, 5]]

        :return: the tiles modified by the transition of ii with jj
        :rtype: TypePuzzle
        """
        tiles = copy.deepcopy(self.tiles)
        tiles[ii[0]][ii[1]], tiles[jj[0]][jj[1]] = (
            tiles[jj[0]][jj[1]],
            tiles[ii[0]][ii[1]],
        )
        return tiles

    def get_index(self, tile: int, tiles: TypePuzzle = None) -> tuple[int, int]:
        """Retrieves the index of a tile in tiles

        For example::

            get_index(0, [[1, 2, 3], [4, 0, 6], [7, 8, 5]])
            wil return (1, 1)

        :param tile: the tile for which we are looking for the index
        :type tile: int
        :param tiles: the list when we need to look for the tile
        :type tiles: TypePuzzle, optional
        :return: the index of the tile in tiles
        :rtype: tuple[int, int]
        """
        tiles = tiles if tiles else self.tiles
        self.check_tiles(tiles)
        tile_index = [item for sublist in tiles for item in sublist].index(tile)
        return tile_index // self.LEN_TILES, tile_index % self.LEN_TILES

    def get_possible_actions(self) -> List[Puzzle]:
        """Check all the possible movements of the puzzle

        We must check the top, bottom, left, right.

        Example::

            [[1, 2, 3],
             [4, 0, 6],
             [7, 8, 5]]
            The possibilities are:
            - Top: 2
            - Left: 4
            - Right: 6
            - Bottom: 8

        :return: All possible moves
        :rtype: List[Puzzle]
        """
        moves: List[Puzzle] = []
        i, j = self.get_index(self.BLANK)

        def add_action(ij_new: tuple[int, int]) -> None:
            """Adds a possible action to the total actions list

            We create a new puzzle (child) taking care to maintain all the father's properties

            :param ij_new: coordinates of possible displacement
            :type ij_new: tuple[int, int]
            :return: None because we just append the action
            """
            tiles_: Puzzle = copy.deepcopy(self)
            tiles_.tiles = self._transition((i, j), ij_new)
            tiles_.cost = self.get_cost(ij_new[0], ij_new[1])
            moves.append(tiles_)

        if i > 0:  # up
            add_action((i - 1, j))
        if j < self.LEN_TILES - 1:  # right
            add_action((i, j + 1))
        if j > 0:  # left
            add_action((i, j - 1))
        if i < self.LEN_TILES - 1:  # down
            add_action((i + 1, j))
        moves.reverse()
        return moves

    def get_cost(self, i, j) -> int:
        """Allows to know the cost of moving the puzzle to a determined location

        We recover the cost of the current puzzle to which we add the cost of the trip.
        The cost of the puzzle is calculated as follows:

        - The cost of the current puzzle + 1 if the tile at location (i, j) is even
        - The cost of the current puzzle + 2 if the tile at location (i, j) is odd

        :param i: location of the line where you want to recover the cost
        :type i: int
        :param j: location of the column where you want to recover the cost
        :type j: int
        :return: the cost if we move to the location (i, j)
        :rtype: int
        """
        return self.cost + (1 if self.tiles[i][j] % 2 == 0 else 2)

    def heuristic_misplaced(self) -> float:
        """Counts the number of misplaced tiles

        We look at the goal state and compare it with our current puzzle.
        We count each tile that is not in its correct location

        :return: the number of misplaced tiles
        :rtype: float
        """
        return sum(
            self.get_cost(i, j)
            for i in range(self.LEN_TILES)
            for j in range(self.LEN_TILES)
            if self.tiles[i][j] != self.GOAL_STATE[i][j]
        )

    def heuristic_manhattan_distance(self) -> float:
        """Counts how much is a tile misplaced from the original position

        :return: the distance that indicates how far the tiles are moved from their original position
        :rtype: float
        """

        def _get_distance(i: int, j: int) -> float:
            """Allows to know the distance of a tile from its desired location (goal state)

            We look::

            - the index of the tile (i, j) in the goal puzzle
            - the index of the tile (i1, j1) in the current puzzle

            Then, we calculate the distance: |i - i1| + |j - j1|

            :param i: line of the tile for which we are looking for the distance
            :type i: int
            :param j: column of the tile for which we are looking for the distance
            :type i: int
            :return: the distance between the current tile and the goal state tile
            :rtype: float
            """
            i1, j1 = self.get_index(self.tiles[i][j], self.GOAL_STATE)
            return abs(i - i1) + abs(j - j1)

        return sum(
            _get_distance(i, j)
            for i in range(self.LEN_TILES)
            for j in range(self.LEN_TILES)
        )

    def is_goal(self) -> bool:
        """Defined if the current puzzle is finished
        i.e. its tiles are equal to the tiles of the goal state

        :return: True if the current puzzle is done (finished), False otherwise
        :rtype: bool
        """
        return self.tiles == self.GOAL_STATE

    @staticmethod
    def puzzles_to_list(list_puzzle: List[Puzzle]) -> List[TypePuzzle]:
        """Turns a Puzzle list into a TypePuzzle list

        :param list_puzzle: the list of puzzle that we want transformed
        :type list_puzzle: List[Puzzle]
        :return: List of Puzzle tiles
        :rtype: List[TypePuzzle]
        """
        return [x.tiles for x in list_puzzle]

    @staticmethod
    def check_tiles(tiles: TypePuzzle) -> None:
        """ Check if the tiles passed as parameters is valid

        :param tiles: a list of lists representing the puzzle matrix.
            For Example [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        :type tiles: TypePuzzle
        :return: True if valid, False otherwise
        :rtype: bool
        """
        if (
            not isinstance(tiles, list)
            or len(tiles) < 0
            or (len(tiles) != len(tiles[0]))
        ):
            raise ValueError("tiles {0} doesn't have the good format".format(tiles))
        # Transform the list to [7, 2, 1, 3, 4, 5, 6..] (for example)
        flat_tiles = sorted([item for sublist in tiles for item in sublist])
        ordered_tiles = list(range(len(tiles) ** 2))
        if not flat_tiles == ordered_tiles:
            raise ValueError(
                "Don't match pattern. Expected {0}, actual {1}".format(
                    ordered_tiles, flat_tiles
                )
            )
