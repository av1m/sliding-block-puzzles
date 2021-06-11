# -*- coding: utf-8 -*-

from .exceptions import *

from .search import Search
from .exceptions import DepthLimitedError
from .breadth_first import BreadthFirst
from .depth_first import DepthFirst
from .a_star import AStar
from .depth_limited import DepthLimited
from .greedy_best_first import GreedyBestFirst
from .iterative_deepening import IterativeDeepening
from .uniform_cost import UniformCost
from .bidirectional import Bidirectional
from .iterative_lengthening import IterativeLengthening
from .iterative_deepening_a_star import IterativeDeepeningAStar


get_algorithm = {
    "a_star": AStar,
    "breadth_first": BreadthFirst,
    "depth_first": DepthFirst,
    "depth_limited": DepthLimited,
    "greedy_best_first": GreedyBestFirst,
    "iterative_deepening": IterativeDeepening,
    "uniform_cost": UniformCost,
    "bidirectional": Bidirectional,
    "iterative_lengthening": IterativeLengthening,
    "iterative_deepening_a_star": IterativeDeepeningAStar,
}
