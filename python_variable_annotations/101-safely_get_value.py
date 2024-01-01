#!/usr/bin/env python3
'''
Simple module for strongly
typed python
'''
from typing import Any, Mapping, TypeVar


T = TypeVar('T', bound=Any)

def safely_get_value(dct: Mapping,
                     key: Any, default: None | T = None
                     ) -> Any | T:
    '''
    Function to safely retrieve a value from
    a dictionary
    '''
    if key in dct:
        return dct[key]
    else:
        return default
