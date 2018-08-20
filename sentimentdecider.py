from pymongo import MongoClient
import os
import itertools

client = MongoClient ("localhost:27017")
db = client.twitter
db.drop_collection ('sentimentdata')
doc = db.twitterdatacopy.find ()

s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
sum = 0
counter = 0
for x in doc:
    if x['m1'] == 'pos':
        s1 = 1
    if x['m2'] == 'pos':
        s2 = 1
    if x['m3'] == 'pos':
        s3 = 1
    if x['m4'] == 'pos':
        s4 = 1
    if x['m5'] == 'pos':
        s5 = 1
    sum = s1 + s2 + s3 + s4 + s5
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    if sum >= 3:
        db.sentimentdata.insert_one (
            {"tweet": x['tweet'], "country": x['country'], "lat": x['location'][0], "lng": x['location'][1]})
    sum = 0
    counter = counter + 1
    print(counter)

os.system ('/Users/mandeepsinghsidhu/Downloads/mongodb/bin/mongoexport --db twitter --collection sentimentdata > plot.json')

f1 = open ('plot.json', 'rb')

f2 = open ('plot.js', 'wb')

for line in f1:
    f2.write (line)
    f2.write (",")

f1.close()
f2.close()


final = []
final1 = []
final2 = []
final3 = []

with open('temp1.html') as f:
    final1 = f.readlines()

with open('plot.js') as f:
    final2 = f.readlines()

with open('temp2.html') as f:
    final3 = f.readlines()


final = itertools.chain(final1,final2, final3)

#print(final1)
#print(final2)
#print(final3)

thefile = open('finalresult.html', 'w')

for item in final:
  thefile.write("%s\n" % item)







