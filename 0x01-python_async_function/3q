#!/usr/bin/env python3
"""
Takes in an integer argument waits for a random delay between 0 and max_delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Returns random delay between 0 and max_delay
    """
    
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
