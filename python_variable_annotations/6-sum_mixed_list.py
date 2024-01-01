#!/usr/bin/env python3
'''
Simple module for strongly
typed python
'''
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    '''
     function sum_mixed_list which takes a list
     input_list of floats or ints as argument
     and returns their sum as a float.
    '''

    return sum(input_list)
