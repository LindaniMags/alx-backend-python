#!/usr/bin/env python3
"""
will execute async_comprehension four times in parallel.
"""
import time
import asyncio
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measures the total runtime and returns it.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total = time.time() - start
    return total
