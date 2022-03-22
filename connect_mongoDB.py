import pymongo

def connect_db(name_db):
    """connect to mongoDB"""
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")  # подключаемся к серверу
    my_db = myclient[name_db]
    return my_db

