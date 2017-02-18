#coding:UTF-8

import pymongo
from pymongo import MongoClient
client = pymongo.MongoClient("localhost", 27017)
db = client.mydb
db.collection_names()
books = db["books"]
type(books)
dir(books)
books.find_one()
db.books.findOne()



