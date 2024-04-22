#!/usr/bin/env python3
""" """
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ asynchronous function  to await random delay"""
    my_list: List[float] = []
    asyn_tasks: List[float] = []
    resolved_list: List[float] = []
    asyn_tasks = [wait_random(max_delay) for _ in range(n)]
    resolved_list = await asyncio.gather(*asyn_tasks)
    my_list.extend(resolved_list)
    return my_list
