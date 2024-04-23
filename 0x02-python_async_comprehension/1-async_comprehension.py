#!/usr/bin/env python3
""" module with one coroutine async_comprehension """
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """The coroutine will collect 10 random numbers
    using an async comprehensing over async_generator"""
    result: List[float] = [_ async for _ in async_generator()]
    return result
