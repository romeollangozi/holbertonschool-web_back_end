#!/usr/bin/env python3
'''
Simple demonstration of
asyncio capabilities
'''
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    '''
    asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random
    that waits for a random delay between 0 and
    max_delay (included and float value) seconds
    and eventually returns it.
    '''

    n = uniform(0, float(max_delay))
    await asyncio.sleep(n)
    return n
