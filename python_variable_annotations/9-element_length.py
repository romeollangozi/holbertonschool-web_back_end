#!/usr/bin/env python3
'''
Simple module for strongly
typed python
'''
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Function that takes as an argument an Iterable
    and returns an list of tuples containing
    the element and its length
    '''

    return [(i, len(i)) for i in lst]
