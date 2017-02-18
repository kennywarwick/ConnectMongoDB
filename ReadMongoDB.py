#coding:UTF-8
import pymongo
import json
from pymongo import MongoClient
client = pymongo.MongoClient('10.120.37.13',27017)
db = client ['project']
collection = db['Expedia']
list = []
cursor = db.All_Comments.find({}, {'_id': False})
for data in cursor:
    list.append(data)

# print type(list)
# print list[0]
# print len(list)
# for i in list[0]:
#     print i
'''
comment_collection
level
hotel
address
'''
count = 0
# for i in list:
    # print i["hotel"].split("(")[0] + "  ,  " + i["address"].replace(" ","").split("TWN")[-1]
    # print i["address"].replace(" ","").split("TWN")[-1]

#     for j in i["comment_collection"]:
#         count = count +1
#         print j["comment"]

    # count = count +1
print count

# print count
    # print i["address"]
# contentjson = json.dumps(list, ensure_ascii=False)
# with open("E:/All_Comments_final.json","w") as w:
#     w.write(contentjson.encode("utf-8"))

