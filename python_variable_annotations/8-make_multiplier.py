#!/usr/bin/env python3
"""module documentation"""
from typing import Callable


# callable function: takes a float and returns a float
def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """callable function"""
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
