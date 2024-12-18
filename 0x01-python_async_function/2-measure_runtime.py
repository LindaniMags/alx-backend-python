#!/usr/bin/env python3
"""
measures the total execution time for wait_n(n, max_delay),
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    returns elapsed time.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop = time.time()
    total_time = stop - start
    return total_time / n
