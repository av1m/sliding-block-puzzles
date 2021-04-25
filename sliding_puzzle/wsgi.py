# coding: utf-8

import json
from typing import List

from flask import Flask, request, Response

from sliding_puzzle.algorithm import get_algorithm
from sliding_puzzle.representation.puzzle import Puzzle

app = Flask(__name__)


def all_diff(solutions: List[Puzzle]) -> List[int]:
    """
    Allows you to collect all the pieces to move to solve the puzzle
    :param solutions: a list of puzzle sorted in the order of the solution.
    The first element is the basic puzzle, the last is the solution
    :return: a list of integers where each integer corresponds to the number of the box to be moved
    """

    def one_diff(puzzle1: Puzzle, puzzle2: Puzzle) -> int:
        """
        Return the cell that has changed between puzzle1 and puzzle2
        We retrieve the index of zero in the second puzzle, then we look at the number of this index in the first puzzle
        :param puzzle1: First Puzzle
        :param puzzle2: Second Puzzle. This must be the first puzzle with one more move
        :return: the element that moved between the first and the second puzzle
        """
        new_pos = puzzle2.get_index(0)
        return puzzle1.tiles[new_pos[0]][new_pos[1]]

    i = 0
    result = []
    while i < len(solutions) - 1:
        result.append(one_diff(solutions[i], solutions[i + 1]))
        i += 1
    return result


@app.route("/", methods=["POST"])
def flutter():
    """
    Web service allowing a Client to interact with the sliding_puzzle application
    The client (here the Flutter application) must make an HTTP POST request and put in the body :
    - tiles: the list of the puzzle. For example [[1, 2, 3], [4, 5, 6], [7, 8, 0]] (in string or int)
    - method: the method used to solve the puzzle

    :return: An HTTP request. In the body are all the moves to perform to solve the puzzle
    """
    tiles = request.values.get("tiles")
    method = request.values.get("method")

    if (not tiles) or (not method) or (method not in get_algorithm.keys()):
        return "Malformed request", 400

    try:
        tiles = json.loads(tiles)

        # The client sends a list with elements that have an offset of 1
        # The client does not return 0, but the largest value
        # For example, for an 8-puzzle, the 0 will be the 8th element (which will be transformed into 9 in tiles_int)
        tile_max = (len(tiles[0]) ** 2) - 1
        tiles_int = [[0 if i == tile_max else int(i) + 1 for i in j] for j in tiles]

        # We solve the puzzle
        puzzle = Puzzle(tiles_int)
        strategy = get_algorithm.get(method)
        strategy = strategy(puzzle)
        strategy.solve()
        solutions = all_diff(strategy.solution)
    except Exception as e:
        return "Malformed request => {}".format(e), 400

    # Create HTTP Response
    response = Response(json.dumps(solutions))
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = True
    response.headers["Access-Control-Allow-Headers"] = (
        "Origin,Content-Type,X-Amz-Date,Authorization,X-Api-Key,"
        "X-Amz-Security-Token,locale "
    )
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"

    return response
