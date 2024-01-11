#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Dataset indexed by sorting position, starting at 0
        """

        indexed_dataset = self.indexed_dataset()
        assert index >= 0 and index < len(indexed_dataset), "out of range"
        assert page_size > 0 and page_size <= len(indexed_dataset),\
            "out of range"

        data = []
        last_index = index
        while len(data) < page_size:
            if last_index not in indexed_dataset.keys():
                last_index = last_index + 1
                continue
            data.append(indexed_dataset[last_index])
            last_index = last_index + 1
        return {
                "index": index,
                "data": data,
                "next_index": last_index,
                "page_size": len(data)
                }
