import xlrd
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import pickle
import numpy as np

workbook = xlrd.open_workbook("trainfinal.xlsx","rb")
sheets = workbook.sheet_names()
train = []

for sheet_name in sheets:
    sh = workbook.sheet_by_name(sheet_name)
    #for rownum in range(4001,sh.nrows):
    for rownum in range(0, 1000):
        row_values = sh.row_values(rownum)
        train.append((row_values[1], row_values[2]))
        #print (row_values[1],row_values[2])


#print required_data
#print len(train)
train_set = np.array(train)
print("classifier started")
classifier = NaiveBayesClassifier(train_set)
print("done classifying")
file_name = 'finalized_modeld.sav'
pickle.dump(classifier,open(file_name,'wb'))




