import math
from pymongo import MongoClient
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

client = MongoClient("localhost:27017")
db = client.twitter
doc = db.twitterdata.find().limit(1000)
for x in doc:
    print x['tweet']
    blob = TextBlob(x['tweet'], analyzer = NaiveBayesAnalyzer())
    print((blob.sentiment))
    if (math.fabs(blob.sentiment[1] - blob.sentiment[2]) > 0.015):
        if (blob.sentiment[1] > blob.sentiment[2]):
            print("1")
            db.sentimentdata.insert_one({"lat":x['location'][0],"lng":x['location'][1]})
        else:
            print("-1")
            #db.sentimentdata.insert_one({"location": x['location'], "sentiment": -1})
    else:
        print("0")
        #db.sentimentdata.insert_one({"location": x['location'], "sentiment": 0})

