#!/usr/bin/env python3
'''
Simple demonstration of
asyncio capabilities
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Function that takes max_delay as int and return
    a asyncio Task object
    '''

    return asyncio.create_task(wait_random(max_delay))
