import pymongo
mongoclient = pymongo.MongoClient("localhost:27017")

userbase = mongoclient["userbase"]

users = userbase["users"]

