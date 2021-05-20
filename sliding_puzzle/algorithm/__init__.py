# coding: utf-8

from .exceptions import *

from .a_star import AStar
from .search import Search
from .breadth_first import BreadthFirst
from .depth_first import DepthFirst
from .depth_limited import DepthLimited
from .exceptions import DepthLimitedError
from .greedy_best_first import GreedyBestFirst
from .iterative_deepening import IterativeDeepening
from .uniform_cost import UniformCost
from .bidirectional import Bidirectional
from .iterative_deepening_a_star import IterativeDeepeningAStar
from .iterative_lengthening import IterativeLengthening


get_algorithm = {
    "a_star": AStar,
    "breadth_first": BreadthFirst,
    "depth_first": DepthFirst,
    "depth_limited": DepthLimited,
    "greedy_best_first": GreedyBestFirst,
    "iterative_deepening": IterativeDeepening,
    "uniform_cost": UniformCost,
    "bidirectional": Bidirectional,
    "iterative_deepening_a_star": IterativeDeepeningAStar,
    "iterative_lengthening": IterativeLengthening,
}
