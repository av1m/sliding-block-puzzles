# coding: utf-8

from enum import Enum


class DepthLimitedError(Enum):
    """Indicates the 'errors' that an algorithm that has a limit can return
    The algorithm may not find support for two reasons :
    - A solution may be possible but we have reached the limit
    - The limit has not been reached and we have not found a solution
    """

    FAILURE = "FAILURE"
    CUTOFF = "CUTOFF"
