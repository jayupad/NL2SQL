# -*- coding: utf-8 -*-
"""RAG Handler
This method processes documentation to be used as a 
reference for the model to augment generation of queries.
"""
from data.loader import Database
from typing import List

class RAGHandler():
    """This class implements RAG on top of the provided documentation in the database 
    to generate relevant queries
    """
    def __init__(self, db: Database, chunk_size: int, overlap_size: int):
        """Initialize RAG Handler to interact with Weaviate

        Args:
            db (Database): Database that stores all available SQL documentation.
            chunk_size (int): Individual chunk size to store in db. # (potentially switch to semantic chunking)
            overlap_size (int): Size of overlap between chunks.
        """
        self.db = db
        self.chunk_size = chunk_size
        self.overlap_size = overlap_size

    def retrieve_and_chunk(self) -> List[str]:
        """Method to retrieve, clean, and chunk SQL documentation data from the internal database.

        Returns:
            list(str): list of chunked text from the document data
        """
        pass
    
    def populate_weaviate(self, transformed_data: List[str], force_refresh: bool) -> bool:
        """Method to store data to the Weaviate database.

        Args:
            transformed_data (list): Data that is prepared for insertion in Weaviate DB.
            force_refresh (bool): Overwrite Weaviate database if data exists and true. 
                If false and data is present, no changes are made to Weaviate.
        
        Returns:
            bool: True if successful, False if failed or database already exists.
        """
        pass

    def generate_with_search(self, prompt_query: str, limit: int, grouped_task: str) -> List[str]:
        """Method to retrieve relevant objects from Weaviate in conjunction with query generation.

        Args:
            prompt_query (str): Prompt that will serve as the basis of query generation.
            limit (int): Maximum number of output queries that will be generated.
            grouped_task (str): Prompt applied to the set of objects in the Weaviate DB found through search.
        
        Returns: 
            list (str): Generated queries that follow from the user query aided by the relevant documentation.
        """
        raise NotImplementedError