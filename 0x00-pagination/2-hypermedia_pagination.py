#!/usr/bin/env python3
""" Hypermedia pagination """


import csv
import math
from typing import List


class Server:
    """ Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> list:
        """ return tha appropriate page of the dataset """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        indexes = index_range(page, page_size)
        try:
            return self.dataset()[indexes[0]:indexes[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ return dictionary of information about page size,
        page, data, next page, previous page, total page
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
def index_range(page: int, page_size: int) -> tuple:
    """Returns the first and last index"""
    return ((page - 1) * page_size, page * page_size)
