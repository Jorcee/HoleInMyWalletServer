import pandas as pd
from pandas.io.json import json_normalize
import json
import csv
import requests
import CleanCSV as clean

class Customer:
    account_id = ""
    cust_id = ""
    types = ["STORE"]
    def make_purchases(self,account):
        url = 'http://api.reimaginebanking.com/accounts/'+account+'/purchases?key=0f030ef091420133d187099758681c3a'
        global types
        types
        merchant_data = open('Merchants.csv','r')
        reader = csv.reader(merchant_data, delimiter=',')
        for t in types:
            for row in reader:
                if any(t in s for s in row):
                    payload={ 'merchant_id': row[0],
                              'medium':'balance',
                              'purchase_date':'2017-10-14',
                              'amount':1,
                              'description':'Bought Stuff'
                    }
                    r = requests.post(url,json=payload)
                
    def make_account(self, cust):
        url = 'http://api.reimaginebanking.com/customers/'+cust+'/accounts?key=0f030ef091420133d187099758681c3a'
        payload = {'type': "Credit Card",
                   'nickname': "Credit Card"+cust,
                   'rewards':0,
                   'balance': 5000,
                   'account_number':cust[0:16]
                   }
        r = requests.post(url,json=payload)
        account_id = json.loads(r.text)
        account_id = account_id['objectCreated']['_id']
        print(account_id)
        self.make_purchases(account_id)
        
    def __init__(self,fname,lname,address, ts=[]):
        global types
        types = ts
        url = 'http://api.reimaginebanking.com/customers?key=0f030ef091420133d187099758681c3a'
        payload={"first_name":fname,
                 "last_name":lname,
                 "address":address
                 }
        r = requests.post(url,json=payload)
        global cust_id
        cust_id = json.loads(r.text)
        cust_id = cust_id['objectCreated']['_id']
        self.make_account(cust_id)

