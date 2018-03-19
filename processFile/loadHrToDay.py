import pandas as pd
import numpy as np
import csv
from statistics import mean

df = pd.read_csv('finaldataset.csv')
loadHr = np.asarray(df['load'])
month = np.asarray(df['monthofyear'])
day = np.asarray(df['weekday'])
date = np.asarray(df['Date'])
dataSize = len(df)
with open('loadDay.csv','w') as myFile:
    writer = csv.writer(myFile)
    writer.writerows([['date','day', 'month', 'loadday']])
    index = 0
    dayList = []
    for i in range(dataSize):
        index = (index+1) % 24
        dayList.append(loadHr[i])
        if index == 0:
            averageDayLoad = mean(dayList)
            writer.writerows([[date[i],day[i],month[i],averageDayLoad]])
            dayList = []

