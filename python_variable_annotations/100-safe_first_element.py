#!/usr/bin/env python3
'''
Simple module for strongly
typed python
'''
from typing import Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> None | Any:
    '''
    Function to return the
    first element of a sequence
    '''

    if lst:
        return lst[0]
    else:
        return None
