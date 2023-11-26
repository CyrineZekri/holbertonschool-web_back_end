#!/usr/bin/env python3
"""module documentation"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes and returns multiple types"""
    return (k, float(v**2))
