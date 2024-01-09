#!/usr/bin/env python3
'''
Module for retrieving data from mongodb
'''


def list_all(mongo_collection):
    '''
    Function to get all documents in a collection
    '''

    return [document for document in mongo_collection.find()]
