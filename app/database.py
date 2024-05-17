from pymongo import MongoClient

def connect_to_mongo():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["blogging_platform"]
    return db
