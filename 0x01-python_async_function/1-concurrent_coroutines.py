#!/usr/bin/env python3
"""module with one function wait_n"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ execute multiple asynchronous tasks """
    my_list: List[float] = []
    asyn_tasks: List[float] = []
    asyn_tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(asyn_tasks):
        res: float = await task
        my_list.append(res)
    return my_list
