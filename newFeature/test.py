import pandas as pd
import numpy as np
from statistics import mean
import csv
from pymongo import MongoClient
# 1456

for y in range(1,11):
    listV = {}
    for j in range(24):
        df = pd.read_csv('T{}_test.csv'.format(y))#pd.DataFrame(list(col.find()))

        dataf = df.dropna()
        # print(len(dataf))
        load = np.asarray(dataf['load'])
        mlis =[]
        for i in range(5):
            mlis.append(float(str(load[(i+j)*24]).encode('ascii')))
        loadList = []
        for i in range(120,len(load)-24,24):
            loadList.append(float(str(load[i+j]).encode('ascii')))

        # print loadList
        v0 = mean(mlis)
        listV[j] = [v0]

        for l in loadList:
            v = (0.1 * l) + (0.9 * v0 )
            v0 = v
            # print(v0,l)
            listV[j].append(v0)
            # with open('features/vn{}_{}.csv'.format(y,j),'a') as myfile:
            #     writer = csv.writer(myfile)
            #     writer.writerows([[v0]])

    with open('testFeature/vntest{}.csv'.format(y),'w') as myfile:
        writer = csv.writer(myfile)
        print len(listV[0])
        writer.writerows([['feature']])
        for i in range(len(listV[0])):
            for tp in range(24):
                writer.writerows([[listV[tp][i]]])





