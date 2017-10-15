from Customer import Customer
import sys
import ast
numto = int(sys.argv[8])
for i in range(0,numto):
    num = sys.argv[3]
    name = sys.argv[4]
    city = sys.argv[5]
    state = sys.argv[6]
    zipc = sys.argv[7]
    types = sys.argv[9].split(" ")
    Customer(sys.argv[1],sys.argv[2]+str(i),{'street_number':num+str(i),
                                             'street_name':name+str(i),
                                             'city':city+str(i),
                                             'state':state,
                                             'zip':zipc},
             types
    )
