import pandas as pd
import locale
import matplotlib.pyplot as plt
from statistics import mean
import csv

for fnum in range(1,11):
    df = pd.read_csv('T{}_v1.csv'.format(fnum))#.format(fnum))
    ld = list(df['load'])
    hour = df['hour']
    date = df['date']
    month = df['month']
    weekday = df['weekday']
    temp = df['Temp']

    with open("finalData/T{}_train.csv".format(fnum),'w') as myFile:
        writer = csv.writer(myFile)
        writer.writerows([['date', 'hour', 'weekday', 'month', 'load','Temp']])
        for i in range(35064):
            writer.writerows([[date[i],hour[i],weekday[i],month[i],ld[i],temp[i]]])
    with open("finalData/T{}_test.csv".format(fnum),'w') as myFile:
        writer = csv.writer(myFile)
        writer.writerows([['date', 'hour', 'weekday', 'month', 'load', 'Temp']])
        for i in range(35064,len(ld)):
            writer.writerows([[date[i], hour[i], weekday[i], month[i], ld[i], temp[i]]])
    print "file {} done".format(fnum)
# print int(str(ld[1]).replace(',',''))
# load = []
# for i in range(len(ld)):
#     num = float(str(ld[i]).replace(',',''))
#     load.append(num)

# print len(load),len(hour),len(date),len(month),len(weekday),len(temp)


# for i in range(len(load)):
#     print (load[i], hour[i])
# load = [ int(ld[i].replace(',','')) for i in range(len(ld)) ]
# load = [ locale.atof(x) for x in ld]
# print( ld[])
# graph_generator(range(1,25),load[:-1],hour[:-1],(1,25))

