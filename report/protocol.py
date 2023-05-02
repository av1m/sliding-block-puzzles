# -*- coding: utf-8 -*-
"""
Module used for the creation of an experiment protocol
We generate random puzzles, with different complexity and size
Then, we submit these puzzles to different algorithms in order to compare them

For a statistical view of the report, see the statistic.py module
"""

from __future__ import annotations

import multiprocessing as mp
import pickle
import time
from typing import List, TypeVar, Callable, Any

from sliding_puzzle import *
from sliding_puzzle.algorithm import get_algorithm

SearchType = TypeVar("SearchType", bound="Search")

N = 10  # Size of generated puzzles
PUZZLE_GENERATED = 2  # How many puzzles the protocol must generate
TIMEOUT_SECONDS = 5  # check the good value
# Name of the file where the report will be saved
REPORT_PICKLE_NAME = f"report_{N}.pickle"


def solve(strategy: SearchType) -> list[SearchType, int]:
    """Find a solution to a puzzle according to the strategy passed in parameter

    This method seems unnecessary but is used to interrupt the algorithm if the timeout has passed.
    Warning ! this method through a timeout can return None

    :param strategy: the strategy used to find a solution to the problem
    :type strategy: SearchType
    :return: A list (tuple) where
            - the first element is the strategy (with the solution completed) and
            - the second an integer which represents the number of Puzzle created
    :rtype: list[SearchType, int]
    """
    if not strategy:
        raise Exception()
    strategy.solve()
    return [strategy, Puzzle.counter]


def timeout(
    func: Callable,
    args: tuple = (),
    kwds=None,
    timeout_seconds: int = 1,
    default: Any = None,
):
    """Run a function and interrupts it if the timeout has passed

    It was inspired by : https://stackoverflow.com/a/13822315/11120444

    :param func: function executed during the timeout
    :type func: function
    :param args: array of arguments that we pass to the function
    :param kwds: keywords arguments
    :type kwds: dict
    :param timeout_seconds: Number of seconds allowed for the execution of the func function
    :type timeout_seconds: int
    :param default: Return if the timeout is exceeded
    :type default: Any
    :return: the default parameter if the timeout is exceeded, otherwise the return of the func function
    :rtype: default or the return of the func function
    """
    if kwds is None:
        kwds = {}
    pool = mp.Pool(processes=1)
    result = pool.apply_async(func, args=args, kwds=kwds)
    try:
        val = result.get(timeout=timeout_seconds)
    except mp.TimeoutError:
        pool.terminate()
        return default
    else:
        pool.close()
        pool.join()
        return val


def start_protocol() -> list[dict]:
    """Starts an experimentation protocol

    This protocol performs the following tasks:

    1. Generate random puzzles (and stores in pickle)
    The number of mutations increases according to the number of puzzle generated
    For example, if we generate 100 puzzle
        - the first puzzle will have 1 mutation,
        - the 50th, 50 mutation and
        - the 100th, 100 mutation

    2. For each puzzle, we run all the research algorithms implemented
    In order not to wait for infinite algorithms, we set a timeout.
    In this sense, an algorithm will not be able to exceed the time allotted to it.

    3. Once the algorithm is finished (whether a solution is found or not), we collect data that we add to an array.

    4. We record this information in a pickle and return the entire report

    :return: the whole algorithm/puzzle report
    :rtype: list[dict]
    """
    # 1. Generate random puzzles

    puzzles: List[Puzzle] = [
        Puzzle.generate_random(n=N, mutations=i) for i in range(1, PUZZLE_GENERATED + 1)
    ]
    # Save and backup the Puzzles
    # pickle.dump(puzzles, open(f"puzzles_{N}.pickle", "wb"))
    # puzzles: List[Puzzle] = pickle.load(open(f"puzzles_{N}.pickle", "rb"))

    # 2. Gathering :
    # - Memory complexity (graph search VS tree search)
    # - Time complexity (number of nodes generated: Puzzle.counter) → Don't forget to reset

    reports: list = []

    i: int
    puzzle: Puzzle
    for i, puzzle in enumerate(puzzles):
        for strategy_name, strategy in get_algorithm.items():
            print(f"Puzzle n°{i + 1}, strategy = {strategy_name}, mutations = {i + 1}")
            Puzzle.counter = 0
            strategy = strategy(puzzle)
            # 3. timeout : use multiprocessing
            # (reminder) strategy can be False !
            res = timeout(
                solve,
                kwds={"strategy": strategy},
                timeout_seconds=TIMEOUT_SECONDS,
                default=False,
            )
            # 4. Generation of report
            # We put many value in 0 because if the puzzle isn't solved, these attribute can be filled
            report = {
                "n": N,
                "mutations": i + 1,
                "puzzle": str(puzzle.tiles),
                "strategy": strategy_name,
                # 4. Heuristic : Compare heuristics
                # - Show that for the same puzzle, the best heuristic will have an inferior result
                # - Running a resolution is shown that we get a better result
                "heuristic_manhattan": HeuristicManhattan.compute(puzzle),
                "heuristic_linear_conflicts": HeuristicLinearConflicts.compute(puzzle),
                "heuristic_misplaced": HeuristicMisplaced.compute(puzzle),
                "cost": 0,
                "expanded_nodes": 0,
                "len_solution": 0,
                "generated_nodes": 0,
                "is_solved": False,
            }
            if res:  # check timeout (success before timeout)
                if res[0].solution:
                    # success before timeout and the algorithm has a solution
                    report["cost"] = res[0].solution[-1].cost
                    report["len_solution"] = len(res[0].solution)
                report["expanded_nodes"] = res[0].expanded_nodes
                report["generated_nodes"] = res[1]
                report["complexity_memory"] = res[0].complexity_memory
                report["is_solved"] = True
            reports.append(report)
            time.sleep(0.5)
    pickle.dump(reports, open(REPORT_PICKLE_NAME, "wb"))
    return reports


if __name__ == "__main__":
    start_time = time.time()
    start_protocol()
    print(f"--- {time.time() - start_time} seconds ---")

    # Show the statistic
    try:
        from .statistic import show_report_statistic

        show_report_statistic(REPORT_PICKLE_NAME)
    except (ImportError, FileNotFoundError) as error:
        print("Can't generate the report : ".format(error))
