from pymongo import MongoClient
import pandas as pd
import numpy as np
import xlsxwriter


client = MongoClient("localhost:27017")
db = client.twitter
doc = db.traningset.find()

workbook = xlsxwriter.Workbook('train.xlsx')
worksheet = workbook.add_worksheet()
row = 0
worksheet.write_string(row,0,"Index")
worksheet.write_string(row,1,"Tweet")
worksheet.write_string(row,2,"Sentiment")
i =0
row = 1
for x in doc:
    i = i +1
    worksheet.write_number(row,0,i)
    worksheet.write_string(row,1,x['tweet'])
    row = row + 1

workbook.close()

