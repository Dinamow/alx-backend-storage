#!/usr/bin/env python3
""" list_all function file """


def list_all(mongo_collection):
    """
    Return a list of all documents in a collection or an empty list
    Args:
        mongo_collection: pymongo collection object
    
    """
    cursor = mongo_collection.find()

    return [doc for doc in cursor]
