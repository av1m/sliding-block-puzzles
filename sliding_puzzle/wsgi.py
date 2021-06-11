# -*- coding: utf-8 -*-

import json
from math import sqrt
from typing import List

from flask import Flask, request, Response, jsonify
from flask_cors import CORS

from sliding_puzzle import Puzzle, TypePuzzle
from sliding_puzzle.algorithm import get_algorithm

app = Flask(__name__)
application = app
CORS(application)


def all_diff(solutions: List[Puzzle]) -> List[int]:
    """Allows you to collect all the pieces to move to solve the puzzle

    :param solutions: a list of puzzle sorted in the order of the solution.
        The first element is the basic puzzle, the last is the solution
    :type solutions: List[Puzzle]
    :return: a list of integers where each integer corresponds to the number of the box to be moved
    :rtype: List[int]
    """

    def one_diff(puzzle1: Puzzle, puzzle2: Puzzle) -> int:
        """Return the cell that has changed between puzzle1 and puzzle2
        We retrieve the index of zero in the second puzzle, then we look at the number of this index in the first puzzle

        :param puzzle1: First Puzzle
        :type puzzle1: Puzzle
        :param puzzle2: Second Puzzle. This must be the first puzzle with one more move
        :type puzzle2: Puzzle
        :return: the element that moved between the first and the second puzzle
        :rtype: int
        """
        new_pos = puzzle2.get_index(0)
        return puzzle1.tiles[new_pos[0]][new_pos[1]]

    i = 0
    result = []
    while i < len(solutions) - 1:
        result.append(one_diff(solutions[i], solutions[i + 1]))
        i += 1
    return result


@app.route("/solve", methods=["POST"])
def main():
    """Web service allowing a Client to interact with the sliding_puzzle application

    The client (here the Flutter application) must make an HTTP POST request and put in the body ::
    - tiles: the list of the puzzle. For example [[1, 2, 3], [4, 5, 6], [7, 8, 0]] (in string or int)
    - method: the method used to solve the puzzle
    - blankAtFirst: True if the blank need to be on the first (top), optional, defaults to True

    :return: An HTTP request. In the body are all the moves to perform to solve the puzzle
    """
    if not request.is_json:
        return jsonify(error=True, message="application/json is not used"), 400

    try:
        data_json = request.get_json(force=True)

        method = data_json.get("method")
        blank_at_first = bool(data_json.get("blankAtFirst", True))
        tiles_tmp = data_json.get("tiles")
        try:
            if isinstance(tiles_tmp, list):
                tiles = tiles_tmp
            else:
                tiles: TypePuzzle = json.loads(tiles_tmp)
        except json.decoder.JSONDecodeError:
            sqrt_tiles = int(sqrt(len([int(t) for t in " ".join(tiles_tmp.split())])))
            tiles: TypePuzzle = [
                tiles_tmp[x : x + sqrt_tiles]
                for x in range(0, len(tiles_tmp), sqrt_tiles)
            ]

        if (not tiles) or (not method) or (method not in get_algorithm.keys()):
            return jsonify(error=True, message="Malformed request"), 400

        # We solve the puzzle
        puzzle: Puzzle = Puzzle(tiles, blank_at_first=blank_at_first)
        strategy = get_algorithm.get(method)
        strategy = strategy(puzzle)
        strategy.solve()
        solutions: List[int] = all_diff(strategy.solution)
    except Exception as e:
        return jsonify(error=True, message="Malformed request", description=e), 400

    # Create HTTP Response
    response = Response(json.dumps({"solutions": solutions}))
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = True
    response.headers["Access-Control-Allow-Headers"] = "Origin,Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS, HEAD"

    return response


@app.route("/", methods=["GET"])
def home():
    """Default path, indicates information about the project

    :return: An HTTP request containing the basic information of the project
    """
    return (
        jsonify(
            url="https://github.com/av1m/sliding-block-puzzles",
            endpoint=[
                {"path": "/", "method": "GET"},
                {"path": "/solve", "method": "POST"},
            ],
        ),
        200,
    )
