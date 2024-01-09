#!/usr/bin/env python3
'''
Module to print status of logs and 
most Methods
'''
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    logs_collection = client.logs.nginx

    print(f"{logs_collection.count_documents({})} logs")
    print(f"\tmethod GET: {logs_collection.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {logs_collection.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {logs_collection.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {logs_collection.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {logs_collection.count_documents({'method': 'DELETE'})}")
    print(f"{logs_collection.count_documents({'path': '/status'})} status check")
