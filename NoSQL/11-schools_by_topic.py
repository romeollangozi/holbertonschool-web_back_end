#!/usr/bin/env python3
'''
Module for retrieving data from mongodb
'''


def schools_by_topic(mongo_collection, topic):
    '''
    Function to inset a school document
    '''

    return mongo_collection.find({"topics": {"$in": [topic]}})
