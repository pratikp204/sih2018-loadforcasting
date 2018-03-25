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


df = pd.read_csv('finaldataset.csv')
hours = np.asarray(df['Hour'])
loadHr = np.asarray(df['load'])

size = len(loadHr)

di = {}
for i in range(1,25):
    di[i]= []
for i in range(size):
    di[hours[i]].append(loadHr[i])

dayMean = {}
dayStdDev = {}

for i in range(1,25):
    hourWiseList = di[i]
    m,sd = getMeanAndStandardDeviation(hourWiseList)
    dayMean[i] = m
    dayStdDev[i] = sd

# print dayMean
# print dayStdDev

with open('scaledHourLoad.csv','w') as myFile:
    writer = csv.writer(myFile)
    writer.writerows([['hour','scaledload']])
    for i in range(size):
        day = hours[i]
        ld = loadHr[i]
        num = ( ld - dayMean[day])/ dayStdDev[day]
        writer.writerows([[day,num]])