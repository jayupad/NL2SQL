# -*- coding: utf-8 -*-
"""Data Loader
This module defines a database that parses raw data into a 
collection of query-prompt pairs, contexts, and code documentation.
"""
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class ColumnData:
    """Represents the data represented by a column of a SQL Table.

    Attributes:
        description: details on the information that is stored in the column. 
        data_type: dtype of the entries in the column.
    """
    description: str
    data_type: str

@dataclass
class QueryPair:
    """Represents the data that models an input/output pair of the NL2SQL model.

    Attributes:
        prompt: Natural language prompt or question corresponding to a SQL context.
        query: SQL query that should provide the data to answer this prompt when executed.
    """
    prompt: str
    query: str

class Database:
    """Stores the contexts, query pairs, and relevant SQL documentation parsed from an external dataset.
    """
    def __init__(self, raw_data: str):
        """Initializes database with data from an external dataset.

        Args:
            raw_data (str): unfiltered data from the external dataset.
        """

        self.contexts = {}
        self.query_pairs = []
        self.documents = []
        self.raw_data = raw_data

    def parse_contexts(self) -> Dict[str, List[ColumnData]]:
        """Method to extracts all context information from raw data.

        Returns:
            dict: A dictionary mapping table names to a list of their columns.
        """
        raise NotImplementedError()

    def parse_queries(self) -> List[QueryPair]:
        """Method to extract all SQL queries and corresponding prompts from raw data.

        Returns:
            list: List of prompt-query pairs.
        """
        raise NotImplementedError()
    
    def parse_documentation(self) -> Dict[str, str]:
        """Method to extract SQL operator documentation from raw data for RAG implementation.

        Returns:
            dict: Dictionary mapping SQL operators to their respective descriptions.
        """
        raise NotImplementedError()
    
    def synthesize_query(self, contexts: List[str]):
        """Method to generate a SQL query utilizing given contexts.

        Returns:
            str: SQL query utilizing a subset of the given contexts.
 
        """
        raise NotImplementedError()
    
