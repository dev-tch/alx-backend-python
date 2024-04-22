#!/usr/bin/env python3
""" module with one function measure_time """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures the total execution time divided by n """
    begin: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.perf_counter()
    return (end - begin) / n
