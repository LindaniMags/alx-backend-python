#!/usr/bin/env python3
"""
Take the code from wait_n and alter it
"""
import asyncio
from typing import List

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    except task_wait_random is being called.
    """
    delays = await asyncio.gather(*(task_wait_random(max_delay)
                                    for _ in range(n)))
    return sorted(delays)
