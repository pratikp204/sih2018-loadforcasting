import pandas as pd
import numpy as np
import csv
from statistics import mean

df = pd.read_csv('loadDay.csv')
loadDay = np.asarray(df['loadday'])
month = np.asarray(df['month'])
dataSize = len(loadDay)
with open('loadMonth.csv','w') as myFile:
    writer = csv.writer(myFile)
    writer.writerows([['month', 'loadmonth']])
    index = 0
    monthList = []
    for i in range(dataSize):
        monthList.append(loadDay[i])

        if i!= dataSize-1:
            x,y = month[i : i+2]
        
        if x != y or i+1 == dataSize:
            averageMonthLoad = mean(monthList)
            writer.writerows([[month[i],averageMonthLoad]])
            monthList = []

