# -*- coding: utf-8 -*-
"""External Data Loader
This module downloads and returns raw data from an external dataset, currently Spider2.
"""
from retry import retry

@retry(tries=3, delay=10, backoff=2, max_delay=60)
def download_data(data_url: str, data_path: str) -> str:
    """Method to download from an external dataset

    Args:
        data_url (str): link to a dataset ideally containing queries, prompts, and documentation
        data_path (str): path to where data will be stored locally

    Returns:
        str: raw data as a string
    """
    raise NotImplementedError()
