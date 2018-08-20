from pymongo import MongoClient

client = MongoClient("localhost:27017")
db = client.twittercopy
db1 = client.twitter
doc = db.twitterdata.find().limit(5000)

for x in doc:
    db1.testingset.insert_one(x)