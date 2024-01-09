#!/usr/bin/env python3
'''
Module for retrieving data from mongodb
'''


def update_topics(mongo_collection, name, topics):
    '''
    Function to inset a school document
    '''

    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
