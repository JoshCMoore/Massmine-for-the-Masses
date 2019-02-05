#loganhornbuckle

# Script to initialize twitterDatabase. There is one collection: tweetInfo, which
# contains all relevant tweet data. The script then deletes the data, leaving only
# the empty collection.

mongo_db_ip = 'mongodb://localhost:27017'

# DO NOT CHANGE THIS PART!#

import pymongo
from pymongo import MongoClient

Client = MongoClient(mongo_db_ip)
twitterDB = Client["twitterDB"]

tweetInfo = twitterDB['tweetInfo']
tweet_data = {
    "created_at":"Thu Jan 31 19:34:47 +0000 2019",
    "id":1091057223990722561,
    "id_str":"1091057223990722561",
    "text":"ITS SNOWING SOOOOO MUCH N WE WENT ON AND ITS ALREADY SETTING AND IT S SSO EXCIITINGGGGGGGG I LOVE SNOW",
    "truncated":False,
    "entities":
    {
      "hashtags":[],
      "symbols":[],
      "user_mentions":[],
      "urls":[]
    },
    "metadata":
    {
      "iso_language_code":"en",
      "result_type":"recent"
    },
    "source":"<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
    "in_reply_to_status_id":None,
    "in_reply_to_status_id_str":None,
    "in_reply_to_user_id":None,
    "in_reply_to_user_id_str":None,
    "in_reply_to_screen_name":None,
    "user":
    {
      "id":983701118009135104,
      "id_str":"983701118009135104",
      "name":"insert emoji here",
      "screen_name":"taekooqs",
      "location":"170219 ♥ 181010",
      "description":"got my first tattoo at 16 it's of Namjoon telling straight people to shut up!",
      "url":"https://t.co/eVLJeyfgWc",
      "entities":
      {
         "url":
         {
            "urls":[{
                  "url":"https://t.co/eVLJeyfgWc",
                  "expanded_url":"http://curiouscat.me/taekooqs",
                  "display_url":"curiouscat.me/taekooqs",
                  "indices":[0,23]}]
         },
         "description":
         {
            "urls":[]
         }
      },
      "protected":False,
      "followers_count":103,
      "friends_count":90,
      "listed_count":4,
      "created_at":"Tue Apr 10 13:39:57 +0000 2018",
      "favourites_count":5011,
      "utc_offset":None,
      "time_zone":None,
      "geo_enabled":False,
      "verified":False,
      "statuses_count":11482,
      "lang":"en",
      "contributors_enabled":False,
      "is_translator":False,
      "is_translation_enabled":False,
      "profile_background_color":"000000",
      "profile_background_image_url":"http://abs.twimg.com/images/themes/theme1/bg.png",
      "profile_background_image_url_https":"https://abs.twimg.com/images/themes/theme1/bg.png",
      "profile_background_tile":False,
      "profile_image_url":"http://pbs.twimg.com/profile_images/1090606656516472832/KPxGU7LL_normal.jpg",
      "profile_image_url_https":"https://pbs.twimg.com/profile_images/1090606656516472832/KPxGU7LL_normal.jpg",
      "profile_banner_url":"https://pbs.twimg.com/profile_banners/983701118009135104/1523368055",
      "profile_link_color":"E27FA7",
      "profile_sidebar_border_color":"000000",
      "profile_sidebar_fill_color":"000000",
      "profile_text_color":"000000",
      "profile_use_background_image":False,
      "has_extended_profile":"true",
      "default_profile":False,
      "default_profile_image":False,
      "following":False,
      "follow_request_sent":False,
      "notifications":False,
      "translator_type":"None"
    },
    "geo":None,
    "coordinates":None,
    "place":None,
    "contributors":None,
    "is_quote_status":False,
    "retweet_count":0,
    "favorite_count":0,
    "favorited":False,
    "retweeted":False,
    "lang":"en"
}
tweetInfo.insert_one(tweet_data)
twitterDB.tweetInfo.remove({'created_at':'Thu Jan 31 19:34:47 +0000 2019'})
