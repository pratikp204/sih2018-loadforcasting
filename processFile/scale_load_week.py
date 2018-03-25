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


df = pd.read_csv('loadDay.csv')
days = np.asarray(df['day'])
loadDays = np.asarray(df['loadday'])

size = len(loadDays)

di = {}
for i in range(1,8):
    di[i]= []
for i in range(size):
    di[days[i]].append(loadDays[i])

dayMean = {}
dayStdDev = {}

for i in range(1,8):
    dayWiseList = di[i]
    m,sd = getMeanAndStandardDeviation(dayWiseList)
    dayMean[i] = m
    dayStdDev[i] = sd

# print dayMean
# print dayStdDev

with open('scaledWeekLoad.csv','w') as myFile:
    writer = csv.writer(myFile)
    writer.writerows([['day','scaledload']])
    for i in range(size):
        day = days[i]
        ld = loadDays[i]
        num = ( ld - dayMean[day])/ dayStdDev[day]
        writer.writerows([[day,num]])