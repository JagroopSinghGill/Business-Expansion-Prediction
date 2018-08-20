import pickle
import textblob as TextBlob
from textblob.classifiers import NaiveBayesClassifier
import xlrd
from pymongo import MongoClient



loaded_model1 = pickle.load(open('finalized_modela.sav','rb'))
loaded_model2 = pickle.load(open('finalized_modelb.sav','rb'))
loaded_model3 = pickle.load(open('finalized_modelc.sav','rb'))
loaded_model4 = pickle.load(open('finalized_modeld.sav','rb'))
loaded_model5 = pickle.load(open('finalized_modele.sav','rb'))

print "loaded"

client = MongoClient("localhost:27017")
db = client.twitter
db.drop_collection('twitterdatacopy')
pipeline=[{"$match": {}},{"$out": "twitterdatacopy"}]
db.twitterdata.aggregate(pipeline)
print "copied"


doc = db.twitterdatacopy.find()

#workbook = xlrd.open_workbook("train.xlsx","rb")
#sheets = workbook.sheet_names()
#train = []
#for sheet_name in sheets:
#    sh = workbook.sheet_by_name(sheet_name)
#    for rownum in range(4990,sh.nrows):
#        row_values = sh.row_values(rownum)
#        print(loaded_model.classify(row_values[1]))
#        print("-----------")

var = 0

for x in doc:
    print(x['tweet'])
    m1 = loaded_model1.classify(x['tweet'])
    m2 = loaded_model2.classify(x['tweet'])
    m3 = loaded_model3.classify(x['tweet'])
    m4 = loaded_model4.classify(x['tweet'])
    m5 = loaded_model5.classify(x['tweet'])
    db.twitterdatacopy.update_one({'_id': x['_id']},{'$set': {'m1': m1,'m2': m2,'m3': m3,'m4': m4,'m5': m5}},upsert=False)
    #db.twitterdatacopy.update_one({'_id': x['_id']}, {'$set': {'m1': m1}},upsert=False)
    #print(m)
    var = var + 1
    print(var)


