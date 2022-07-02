from pymongo import MongoClient
from secrets import CONNECTION_STRING

def get_database():

    
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['songs']
    


def insertRecord(item):
    database = get_database()
    collection = database['songdata']
    collection.insert_one(item)

def insertMany(items):
    database = get_database()
    collection = database['songdata']
    collection.insert_many(items)
