#!/usr/bin/env python3
'''
Module to help for pagination
'''
import csv
import math
from typing import List, Dict


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        Method to return the page and its data
        '''

        assert isinstance(page, int), "page must be an int"
        assert isinstance(page_size, int), "page_size must be an int"
        assert page > 0, "page number must be greater than 0"
        assert page_size > 0, "page_size must be greater than 0"

        start, end = index_range(page, page_size)
        return [[data] for data in self.dataset()[start:end]]

    def get_hyper(self, page: int = 1,
                  page_size: int = 10
                  ) -> Dict[str, any]:
        '''
        Method to return a http body response
        '''
        '''
        assert isinstance(page, int), "page must be an int"
        assert isinstance(page_size, int), "page_size must be an int"
        assert page > 0, "page number must be greater than 0"
        assert page_size > 0, "page_size must be greater than 0"
        '''
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 0 else None,
            "total_pages": total_pages
        }
