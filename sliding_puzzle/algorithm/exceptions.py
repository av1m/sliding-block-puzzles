# coding: utf-8
from enum import Enum


class DepthLimitedError(Enum):
    FAILURE = "FAILURE"
    CUTOFF = "CUTOFF"
