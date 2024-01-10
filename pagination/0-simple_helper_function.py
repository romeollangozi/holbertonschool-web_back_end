#!/usr/bin/env python3
'''
Module to help for pagination
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    The function should return a tuple of size two containing a start
    index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters.
    '''

    offset = page_size * page
    return (offset - page_size, offset)
