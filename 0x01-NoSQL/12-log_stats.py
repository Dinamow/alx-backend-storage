#!/usr/bin/env python3

'''A Python module tha provides stats about nginx'''

from pymongo import MongoClient


if __name__ == '__main__':
    '''Prints the log stats in nginx collection'''
    con = MongoClient('mongodb://localhost:27017')
    collection = con.logs.nginx
    x = collection.estimated_document_count()
    print(f'{x} logs')

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')

    for req in methods:
        print('\tmethod {}: {}'.format(req,
              collection.count_documents({'method': req})))

    print('{} status check'.format(collection.count_documents(
          {'method': 'GET', 'path': '/status'})))
