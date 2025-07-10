# -*- coding: utf-8 -*-
""" Data Loader
This module defines a database that parses raw data into a 
collection of query-prompt pairs, contexts, and code documentation.
"""
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class ColumnData:
    description: str
    data_type: str

@dataclass
class QueryPair:
    sql_query: str
    nl_prompt: str

class Database:
    """Stores the contexts, query pairs, and relevant SQL documentation parsed from an external dataset 
    """
    def __init__(self, raw_data):

        self.contexts = {}
        self.query_pairs = []
        self.documents = []
        self.raw_data = raw_data

    def parse_contexts(self, raw_data) -> Dict[str, List[ColumnData]]:
        """
        Method to extracts all context information from raw data.

        Args:
            raw_data (str): unfiltered data from the external dataset

        Returns:
            dict: A dictionary mapping table names to a list of their columns
        """
        raise NotImplementedError()

    def parse_queries(self, raw_data) -> List[QueryPair]:
        """
        Method to extract all SQL queries and corresponding natural language prompts from raw data

        Args:
            raw_data (str): unfiltered data from the external dataset

        Returns:
            list: A list of prompt-query pairs
        """
        raise NotImplementedError()
    
    def parse_documentation(self) -> Dict[str, str]:
        """
        A method to extract SQL operator documentation from raw data for RAG implementation

        Args:
            raw_data (str): unfiltered data from the external dataset

        Returns:
            dict: A dictionary mapping SQL operators to their respective descriptions 
        """
        raise NotImplementedError()
    
    def synthesize_query(self, contexts: List[str]):
        """
        A method to generate a SQL query utilizing given contexts

        Args:
            contexts (list): unfiltered data from the external dataset

        Returns:
            str: A SQL query utilizing a subset of the given contexts
 
        """
        raise NotImplementedError()
    
