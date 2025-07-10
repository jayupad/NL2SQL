# -*- coding: utf-8 -*-
""" Data Loader
This module downloads and parses data from the Spider2 dataset into a 
database of query-prompt pairs, contexts, and documentation.
"""

class ColumnData:
    """ ColumnData includes description of entries and data type """
    def __init__(self, description: str, data_type: str):
        self.description = description
        self.data_type = data_type

class QueryPair:
    """ Template for data pair consisting of natural language prompt and corresponding sql query """
    def __init__(self, sql_query: str, nl_prompt: str):
        self.query = sql_query
        self.prompt = nl_prompt

class Database:
    '''
    Stores the contexts, query pairs, and relevant SQL documentation parsed from an external dataset 
    '''
    def __init__(self, dataset_url: str, dataset_path: str):

        self.contexts = {}
        self.query_pairs = []
        self.documents = []
        self.raw_data = ""

        self.dataset_url = dataset_url
        self.dataset_path = dataset_path
        self.download_data()

    def download_data(self):
        """
        Downloads and stores data from external dataset to memory
        Stores result in raw_data field
        """
        raise NotImplementedError()

    def parse_contexts(self) -> dict[str, list[ColumnData]]:
        """
        Extracts all contexts from raw data.
        Stores result in a dict mapping table name to all Contexts
        """
        raise NotImplementedError()

    def parse_queries(self) -> list[QueryPair]:
        """
        Extracts SQL queries and natural language prompts from raw data
        Stores and returns a list of these pairs 
        """
        raise NotImplementedError()
    
    def parse_documentation(self) -> list[str]:
        """
        Extracts SQL operator documentation from raw data
        Stores and returns list of all available documentation
        """
        raise NotImplementedError()
    
    def synthesize_query(contexts: list[str]):
        """
        Generates a SQL query utilizing available contexts 
        """
        raise NotImplementedError()
    