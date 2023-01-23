#!/usr/bin/env python3
"""defines Helper Function"""


def index_range(page, page_size):
    """return a tuple of size two containing a start index and an end index
    """
    return ((page - 1) * page_size, page * page_size)
