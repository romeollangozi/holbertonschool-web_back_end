#!/usr/bin/env python3
'''
Simple demonstration of
asyncio capabilities
'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in
    ascending order without using sort() because of concurrency.
    '''

    res = await asyncio.gather(*(task_wait_random(max_delay)
                                 for _ in range(n)))

    return sorted(res)
