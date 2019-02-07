#!/usr/bin/env python3

#This field shouldn't change, but if the mongo database is on a special port or ip then change this variable to be used later on

mongo_db_ip = 'mongodb://localhost:27017'

# DO NOT CHANGE THIS PART!#

import pymongo
from pymongo import MongoClient



client = MongoClient(mongo_db_ip)
analysisdatabase = client["analysisdatabase"]

analysiscollection = analysisdatabase["analysiscollection"]
#database name will have to be changed, not db., I don't know name of twitter fields though
analysis_test_data = {'query_id':'sort_by_date',
                      'query':'db.inventory.find( {date: inserthere } )',

                      'query_id':2,
                      'query':'db.inventory.find( {id: \"114749583439036416\" } )',

                      'query_id': 3,
                      'query': 'db.inventory.find( {quote_count: 1138} )',

                      'query_id': 4,
                      'query': 'db.inventory.find( {reply_count: 1111 } )'}
#combos? How many times was a tweet retweeted that day?
#
analysiscollection.insert_one(analysis_test_data)
#analysisdatabase.analysiscollection.remove({'id':''})
