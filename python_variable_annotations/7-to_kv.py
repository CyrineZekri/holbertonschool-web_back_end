#!/usr/bin/env python3
"""module documentation"""
from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """takes and returns multiple types"""
    return (k, float(v**2))
