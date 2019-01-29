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
userdatabase = client["userdatabase"]

#initialize user collection and delete temp user used for creation
usercollection = userdatabase["usercollection"]
user_test_data = {'username':'Luke Skywalker', 'encryptedPassword':'thisisabadpassword'}
usercollection.insert_one(user_test_data)
userdatabase.usercollection.remove({'username':'Luke Skywalker'})

#initialize oauth collection and delete temp data used for creation
oauthcollection = userdatabase["oauthcollection"]
oauth_test_data = {'username':'Leia Organa', 'oauthkey':'00000000000000'}
oauthcollection.insert_one(oauth_test_data)
userdatabase.oauthcollection.remove({'username':'Leia Organa'})

#All done! Go have fun:)
