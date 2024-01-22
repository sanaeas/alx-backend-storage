#!/usr/bin/env python3
""" list_all function """


def list_all(mongo_collection):
    """List all documents in a MongoDB collection"""
    return [doc for doc in mongo_collection.find()]
