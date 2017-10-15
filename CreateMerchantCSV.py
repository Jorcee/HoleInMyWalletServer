import pandas as pd
from pandas.io.json import json_normalize
import OutputCSV as ocsv
import json
import csv
import ast
import CleanCSV as clean
url = "http://api.reimaginebanking.com/merchants?lat=33.775618&lng=-84.396285&rad=50&key=0f030ef091420133d187099758681c3a&page="
users = pd.read_json(url,typ='series')
page = 2
checker = pd.read_json(url,typ='series')
while page != 12:
    users['data'] += pd.read_json(url+str(page),typ='series')['data']
    checker =  pd.read_json(url+str(page),typ='series')
    page+=1
thing = json_normalize(users['data'][1])
merchant = pd.DataFrame.from_dict(thing)
for i in range(1,200):
    thing = json_normalize(users['data'][i])
    merchant = merchant.append(pd.DataFrame.from_dict(thing))
merchant.to_csv("users.csv",index=False,header=False)
oldCSV = pd.read_csv("users.csv")
oldCSV.to_csv("users.csv",index=False,header=False)
merchantCSV = oldCSV[oldCSV.columns[0]]
nameColumn = oldCSV[oldCSV.columns[9]]
oldCSV.drop(oldCSV.columns[[1,2,3,4,5,7,9]],axis=1,inplace=True)
newCSV = pd.DataFrame()
tagList = []
merchantList = []
for i in range(0,len(nameColumn)):
    if len(nameColumn.iloc[i]) > 50:
        nameColumn.iloc[i] = nameColumn.iloc[i][0:50]
for row in oldCSV.iterrows():
    merchantList.append(row[0])
for row in oldCSV.iterrows():
    tags = ast.literal_eval(row[1][1])
    counter=0
    tags = ["Type=" + x for x in tags]
    tagList.append(tags)
merchantCSV.to_csv("debug.csv",index=False,header=False)
newCSV = pd.DataFrame(tagList)
newCSV.insert(0,'ID',merchantCSV)
newCSV.insert(1,'Name',nameColumn)
for i in range(0,199):
    newCSV.iloc[i] = newCSV.iloc[i].str.upper()
newCSV.to_csv("Merchants.csv",index=False,header=False)
clean.clean_csv("Merchants.csv")
