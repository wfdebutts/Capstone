import numpy as np
import pandas as pd
import csv

keys=pd.read_csv("adjData/maryland.csv")
adjSet=pd.read_csv("adjData/nlist.csv")
keyList=keys[['TRACTID']]
print ('Data Loaded')
adjSet.dtypes
input ('Start querries')
for i in range(1, keyList.shape[0]):
    key = keyList.iloc[i]['TRACTID']
    print(key)
    input('step')
    foo = adjSet[adjSet.NEIGHBOR_TRACTID == key] #querry
input ('Press to End')
