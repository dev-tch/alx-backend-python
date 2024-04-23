#!/usr/bin/env python3
""" module with one coroutine measure_runtime """
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """  execute async_comprehension four times in parallel"""
    begin: float = time.perf_counter()
    async_tasks: List[asyncio.Task] = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*async_tasks)
    end: float = time.perf_counter()
    return (end - begin)
