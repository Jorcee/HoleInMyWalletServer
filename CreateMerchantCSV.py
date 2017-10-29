import pandas as pd
from pandas.io.json import json_normalize
import OutputCSV as ocsv
import json
import csv
import ast
import CleanCSV as clean
#######################
#url of Capital One Merchant Requesgt
url = "http://api.reimaginebanking.com/merchants?&key=0f030ef091420133d187099758681c3a&page="
#get first page of merchants
users = pd.read_json(url,typ='series')
page = 2
checker = pd.read_json(url,typ='series')
#add the rest of the pages
while page != 12:
    users['data'] += pd.read_json(url+str(page),typ='series')['data']
    checker =  pd.read_json(url+str(page),typ='series')
    page+=1
#normalize to prepare for DataFrame    
thing = json_normalize(users['data'][1])
merchant = pd.DataFrame.from_dict(thing)
for i in range(1,100):
    thing = json_normalize(users['data'][i])
    merchant = merchant.append(pd.DataFrame.from_dict(thing))
merchant.to_csv("users.csv",index=False,header=False)
oldCSV = pd.read_csv("users.csv")
merchantCSV = oldCSV[oldCSV.columns[0]]
#save the name
nameColumn = oldCSV[oldCSV.columns[1]]
#drop uneeded info about the flag
oldCSV.drop(oldCSV.columns[[1,2,3,4,5,6,7,9,10,11]],axis=1,inplace=True)
newCSV = pd.DataFrame()
tagList = []
merchantList = []
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
for i in range(0,99):
    newCSV.iloc[i] = newCSV.iloc[i].str.upper()
newCSV.to_csv("Merchants.csv",index=False,header=False)
clean.clean_csv("Merchants.csv")
