# -*- coding: utf-8 -*-
"""Context Filtering
This module filters out irrelevant context from all available context based on the user's request.
"""
from typing import List, Dict
from data.loader import Database, ColumnData

def retrieve_table_list(db: Database) -> List[str]:
    """Method to prompt user to specify which tables are necessary for their query.
    
    Args:
        db (Database): Database that stores all available context information.
    
    Returns:
        list: List of table names to be utilized for query generation. 
        Returns all available table names if unspecified by user.
    """
    pass

def context_filter(database: Database) -> List[Dict[str, ColumnData]]:
    """Method to select only contexts from the tables specified by the user.
    
    Args:
        db (Database): Database that stores all available context information
    
    Returns:
        list(dict): List of column name-data mappings to be utilized for query generation. 
    """
    pass