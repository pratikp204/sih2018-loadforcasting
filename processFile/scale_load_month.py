import math
from statistics import mean
import pandas as pd
import numpy as np
import csv

def getMeanAndStandardDeviation(listX):
    xmean = mean(listX)
    total = 0.
    n =len(listX)
    for i in range(n):
        total += pow((listX[i]-xmean),2)
    variance = total / n
    sd = math.sqrt(variance)
    return xmean,sd


df = pd.read_csv('loadMonth.csv')
months = np.asarray(df['month'])
loadMonths = np.asarray(df['loadmonth'])

size = len(loadMonths)

di = {}
for i in range(1,13):
    di[i]= []
for i in range(size):
    di[months[i]].append(loadMonths[i])

dayMean = {}
dayStdDev = {}

for i in range(1,13):
    dayWiseList = di[i]
    m,sd = getMeanAndStandardDeviation(dayWiseList)
    dayMean[i] = m
    dayStdDev[i] = sd

# print dayMean
# print dayStdDev

with open('scaledMonthLoad.csv','w') as myFile:
    writer = csv.writer(myFile)
    writer.writerows([['month','scaledload']])
    for i in range(size):
        mn = months[i]
        ld = loadMonths[i]
        num = ( ld - dayMean[mn])/ dayStdDev[mn]
        writer.writerows([[mn,num]])