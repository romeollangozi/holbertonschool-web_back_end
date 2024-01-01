#!/usr/bin/env python3
'''
Simple module for strongly
typed python
'''
from typing import Callable, Union


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
     function make_multiplier that takes a
     float multiplier as argument
     and returns a function that multiplies a
     float by multiplier
    '''

    def function(number):
        return number * multiplier
    return function
