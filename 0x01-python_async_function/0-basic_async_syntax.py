#!/usr/bin/env python3
""" module with one function"""
from random import uniform
from asyncio import sleep


async def wait_random(max_delay=10):
    """ asynchronous function  to await random delay"""
    random_delay = uniform(0, max_delay)
    await sleep(random_delay)
    return random_delay
