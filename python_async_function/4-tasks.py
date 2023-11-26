#!/usr/bin/env python3
"""module documentation"""
import asyncio
from typing import List

# Assuming task_wait_random is in the same module as wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """function documentation"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_delays = [await task for task in asyncio.as_completed(tasks)]
    return completed_delays
