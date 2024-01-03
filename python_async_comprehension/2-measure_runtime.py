#!/usr/bin/env python3
'''
Python - Async Comprehension
Module
'''
import asyncio
from typing import List
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
     measure_runtime should measure the
     total runtime and return it.
    '''
    start = time.time()
    result = await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time() - start
    return end
