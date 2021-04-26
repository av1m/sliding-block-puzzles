# coding: utf-8

from sliding_puzzle.algorithm.a_star import AStar
from sliding_puzzle.algorithm.breadth_first import BreadthFirst
from sliding_puzzle.algorithm.depth_first import DepthFirst
from sliding_puzzle.algorithm.depth_limited import DepthLimited
from sliding_puzzle.algorithm.greedy_best_first import GreedyBestFirst
from sliding_puzzle.algorithm.iterative_deepening import IterativeDeepening
from sliding_puzzle.algorithm.uniform_cost import UniformCost

get_algorithm = {
    "a_star": AStar,
    "breadth_first": BreadthFirst,
    "depth_first": DepthFirst,
    "depth_limited": DepthLimited,
    "greedy_best_first": GreedyBestFirst,
    "iterative_deepening": IterativeDeepening,
    "uniform_cost": UniformCost,
}
