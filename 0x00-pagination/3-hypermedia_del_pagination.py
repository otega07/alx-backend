#!/usr/bin/env python3
"""Hypermedia pagination sample.
"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance.
        """
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
        """Creates an indexed dataset
        """
        if self.__indexed_dataset is None:
            self.__indexed_dataset = {
                    i: data for i, data in enumerate(self.dataset())
            }
            return self.__indexed_dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retrieves information about a page.
        """
        page_data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if end < len(self.__dataset) else None,
            'prev_page': page - 1 if start > 0 else None,
            'total_pages': total_pages,
        }
        return page_info

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieves Hypermedia index page information
        """
        assert type(index) == int and type(page_size) == int
        assert index >= 0 and pae_size > 0

        indexed_data = self.indexed_dataset()
        dataset_size = len(self.indexed_dataset)
        data = []

        for i in range(index, min(index + page_size, dataset_size)):
            data.append(indexed_data.get(i))

        next_indexed = index + page_size if index + page_size < dataset_size else None
        page_info = {
            'index': index,
            'next_index': next_index,
            'page_size': len(data_page),
            'data': data_page
        }
        return page_info
