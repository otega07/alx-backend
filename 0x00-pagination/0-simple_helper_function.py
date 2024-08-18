#!/usr/bin/env python3
"""Pagination helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculates the start and end index for pagination based on page number and page size."""
    # The end index is simply the product of the page number and page size
    end = page * page_size
    
    # The start index is derived by subtracting the page size from the end index
    start = end - page_size
    
    return (start, end)
