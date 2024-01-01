#!/usr/bin/env python3
'''
Simple demonstration of
asyncio capabilities
'''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    function with integers n and max_delay as arguments that
    measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n. Your function should return a float
    '''
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
