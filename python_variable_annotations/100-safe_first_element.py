#!/usr/bin/env python3
'''
Simple module for strongly
typed python
'''
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[any]) -> Union[Any, None]:
    '''
    Function to return the
    first element of a sequence
    '''

    if lst:
        return lst[0]
    else:
        return None
