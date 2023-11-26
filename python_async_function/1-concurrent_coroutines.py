#!/usr/bin/env python3
"""module documentation"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function documentation"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_delays = [await task for task in asyncio.as_completed(tasks)]
    return completed_delays
