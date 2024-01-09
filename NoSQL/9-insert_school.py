#!/usr/bin/env python3
'''
Module for retrieving data from mongodb
'''


def insert_school(mongo_collection, **kwargs):
    '''
    Function to inset a school document
    '''

    return (mongo_collection.insertOne(kwargs)).inserted_id