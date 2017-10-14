import pandas as pd
from pandas.io.json import json_normalize
import OutputCSV as ocsv
import json
import csv
import ast
users = pd.read_json('http://api.reimaginebanking.com/merchants?key=0f030ef091420133d187099758681c3a&page=',typ='series')
for i in range(2,236):
    users['data'] += pd.read_json('http://api.reimaginebanking.com/merchants?key=0f030ef091420133d187099758681c3a&page='+str(i),typ='series')['data']
thing = json_normalize(users['data'][1])
merchant = pd.DataFrame.from_dict(thing)
for i in range(2,3000):
    thing = json_normalize(users['data'][i])
    merchant = merchant.append(pd.DataFrame.from_dict(thing))
merchant.to_csv("users.csv",index=False,header=False)
oldCSV = pd.read_csv("users.csv")
oldCSV.drop(oldCSV.columns[[1,2,3,4,5,6,7,9,10,11]],axis=1,inplace=True)
newCSV = pd.DataFrame()
tagList = []
for row in oldCSV.iterrows():
    tags = ast.literal_eval(row[1][1])
    tagList.append(tags)
newCSV = pd.DataFrame(tagList)
newCSV.insert(0,'ID',oldCSV.columns[0])
newCSV.to_csv("nusers.csv",index=False,header=False)
oldCSV.to_csv("users.csv",index=False,header=False)
