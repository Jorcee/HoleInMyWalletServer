import pandas as pd
from pandas.io.json import json_normalize
import OutputCSV as ocsv
import json
import csv
import ast
import CleanCSV as cleaner

url = "http://api.reimaginebanking.com/customers?key=0f030ef091420133d187099758681c3a"
customers = pd.read_json(url,typ='series')
customerIDs = []
for customer in customers:
    customerIDs.append(customer["_id"])
accountIDs = []
for customerID in customerIDs:
    accounts = pd.read_json("http://api.reimaginebanking.com/customers/"+customerID+"/accounts?key=0f030ef091420133d187099758681c3a",typ='series')
    for account in accounts:
        accountIDs.append(account["_id"])
account_and_purchases = {}
merchantIDs = []
for accountID in accountIDs:
    url = "http://api.reimaginebanking.com/accounts/"+accountID+"/purchases?key=0f030ef091420133d187099758681c3a"
    purchases = pd.read_json(url,typ='series')
    for purchase in purchases:
        merchantIDs.append([accountID,purchase["merchant_id"]])
    account_and_purchases[accountID] = merchantIDs
    for i in range(len(account_and_purchases[accountID]),500):
        account_and_purchases[accountID].append(" ")
    merchantIDs = []
oldCSV = pd.DataFrame.from_dict(account_and_purchases)
newCSV =pd.DataFrame()
for column in oldCSV:
    newCSV = newCSV.append(oldCSV[column].apply(pd.Series))
newCSV.to_csv("dirtyCustomers.csv",index=False,header=False)
cleaner.clean_csv("dirtyCustomers.csv")
    

