#!/usr/bin/env python3

#patanzer

#This script will initialize the userdatabase, which has two collections. 
#The first collection is usercollection, which contains documents that have two fields in addition to the automatic id: username, and encryptedPassword.
#The second collection is the useroauthcollection, which contains documents that have two fields in addition to the automatic id: username, and oauthkey.

#This field shouldn't change, but if the mongo database is on a special port or ip then change this variable to be used later on

mongo_db_ip = 'mongodb://localhost:27017'

# DO NOT CHANGE THIS PART!#

import pymongo
from pymongo import MongoClient

client = MongoClient(mongo_db_ip)
user_database = client["user_database"]

#initialize user collection and delete temp user used for creation
user_collection = user_database["user_collection"]
user_test_data = {'username':'Luke Skywalker', 'encrypted_password':'thisisabadpassword'}
user_collection.insert_one(user_test_data)
user_database.user_collection.remove({'username':'Luke Skywalker'})

#initialize oauth collection and delete temp data used for creation
oauth_collection = user_database["oauth_collection"]
oauth_test_data = {'username':'Leia Organa', 'oauth_key':'00000000000000'}
oauth_collection.insert_one(oauth_test_data)
user_database.oauth_collection.remove({'username':'Leia Organa'})

#initialize study collection and delete temp data used for creation
study_collection = user_database["study_collection"]
study_test_data = {'username': 'Luke Skywalker', 'study_id': '3263827'}
study_collection.insert_one(study_test_data)
user_database.study_collection.remove({'username': 'Luke Skywalker'})

#All done! Go have fun:)
