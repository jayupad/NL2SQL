# -*- coding: utf-8 -*-
"""Prompter 
This module provides a framework for guiding the user to 
structure effective NL prompts
"""
from prompting.context_filter import context_filter
from data.loader import Database
from prompting.rag_handler import RAGHandler

class Prompter:
    """This class handles the prompt engineering from start to finish.
    It will integrate context filtering and RAG in the prompting process
    """
    def __init__(self, db: Database):
        """Initialize Prompter with required data and defines a RAGHandler on the current database
        Args:
            db (Database): Stores documentation for RAG and available contexts
        """
        self.db = db
        self.rag = RAGHandler(self.db)
    
    def prompt_user(self):
        """Method to prompt user for context and search/query weaviate database for 
        retrieval-augmented generation of SQL queries
        """
        pass
