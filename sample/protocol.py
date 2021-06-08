# coding=utf-8


from __future__ import annotations

import multiprocessing as mp
import pickle
import time
from typing import List, TypeVar

from sliding_puzzle import *
from sliding_puzzle.algorithm import get_algorithm

SearchType = TypeVar("SearchType", bound="Search")

N = 3
PUZZLE_GENERATED = 1
MUTATIONS = 5  # check the good value
TIMEOUT_SECONDS = 5  # check the good value
STEP = ...
LIMIT = ...


def solve(strategy: SearchType):
    if not strategy:
        raise Exception()
    strategy.solve()
    return [strategy, Puzzle.counter]


def timeout(func, args=(), kwds=None, timeout=1, default=None):
    """https://stackoverflow.com/a/13822315/11120444"""
    if kwds is None:
        kwds = {}
    pool = mp.Pool(processes=1)
    result = pool.apply_async(func, args=args, kwds=kwds)
    try:
        val = result.get(timeout=timeout)
    except mp.TimeoutError:
        pool.terminate()
        return default
    else:
        pool.close()
        pool.join()
        return val


def run():
    # 1. Generate random puzzles
    # Number of Puzzle generated = 20
    # Number of mutations : 1, 5, 10, 15, 20, ... (to see in function)
    # Puzzle Size = 3, 4, 5, ... (to see in function)
    # blank_at_first = True

    puzzles: List[Puzzle] = [
        Puzzle.generate_random(n=N, mutations=MUTATIONS)
        for _ in range(0, PUZZLE_GENERATED)
    ]
    # pickle.dump(puzzles, open("puzzles.pickle", "wb"))
    # puzzles: List[Puzzle] = pickle.load(open("puzzles.pickle", "rb"))

    # 2. Save :
    # - Complexite memoire (utiliser les performances?)
    #    graph search VS tree search
    # - Time complexity (number of nodes generated: Puzzle.counter) → Don't forget to reset

    reports = []

    for (i, puzzle) in enumerate(puzzles):
        for strategy_name, strategy in get_algorithm.items():
            print("Puzzle n°{}, strategy = {}".format(i, strategy_name))
            Puzzle.counter = 0
            strategy = strategy(puzzle)
            # 3. timeout (multiprocessing)
            # strategy can be False !
            res = timeout(
                solve,
                kwds={"strategy": strategy},
                timeout=TIMEOUT_SECONDS,
                default=False,
            )
            report = {
                "n": N,
                "mutations": MUTATIONS,
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
                "generated_nodes": 0,
                "is_solved": False,
            }
            if res:  # check timeout (success before timeout)
                if res[
                    0
                ].solution:  # success before timeout and the algorithm has a solution
                    report["cost"] = res[0].solution[-1].cost
                report["expanded_nodes"] = res[0].expanded_nodes
                report["generated_nodes"] = res[1]
                report["complexity_memory"] = res[0].complexity_memory
                report["is_solved"] = True
            reports.append(report)
            time.sleep(0.5)
    pickle.dump(reports, open("report.pickle", "wb"))


if __name__ == "__main__":
    run()
