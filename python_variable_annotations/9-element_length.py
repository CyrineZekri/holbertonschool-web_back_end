#!/usr/bin/env python3
"""module documentation"""
from typing import List, Tuple, Sequence, Iterable
# list can take any type thus sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function documentation"""
    return [(i, len(i)) for i in lst]
