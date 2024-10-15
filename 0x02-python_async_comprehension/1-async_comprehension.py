#!/usr/bin/env python3
"""
collects 10 random numbers using an async comprehensing over async_generator
"""
from importlib import import_module as using
from typing import List

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    returns the 10 random numbers.
    """
    return [val async for val in async_generator()]
