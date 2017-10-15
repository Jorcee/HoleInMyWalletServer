import pandas as pd
from pandas.io.json import json_normalize
import json
import csv
cheap = ["SUBWAY", "CONVENIENCE", "TAKEAWAY", "DELIVERY"]
medium = ["BAR", "RESTAURANT", "CAFE", "BAKERY", "STORE", "PHARMACY", "HAIR_CARE", "ELECTRONICS_STORE", "CLOTHING"]
expensive = ["DEPARTMENT_STORE", "JEWELRY_STORE", "SPA", "FINANCE", "FURNITURE_STORE"]

lines =[]
merchant_data = open('Merchants.csv','r')
reader = csv.reader(merchant_data, delimiter=',')
for e in expensive:
    for row in reader:
        if any(e in s for s in row):
            lines.append(row+["COST=HIGH"])
        else:
            for m in medium:
                if any(m in ss for ss in row):
                    lines.append(row+["COST=MODERATE"])
                else:
                    for c in cheap:
                        if any(c in sss for sss in row):
                            lines.append(row+['COST=LOW'])
with open('MerchantsWithCost.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    for row in lines:
        writer.writerow(row)


            
    
