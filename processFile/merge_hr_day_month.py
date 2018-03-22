import numpy as np
import csv
import pandas as pd

df = pd.read_csv('finaldataset.csv')
fd_month = np.asarray(df['monthofyear'])
fd_day = np.asarray(df['weekday'])
fd_date = np.asarray(df['Date'])
fd_hour = np.asarray(df['Hour'])
fd_load = np.asarray(df['load'])
fd_prevload = np.asarray(df['prevload'])
fd_temp = np.asarray(df['temp'])
fd_humid = np.asarray(df['humid'])
fd_windspd = np.asarray(df['windspd'])

sc_hour = pd.read_csv('scaledHourLoad.csv')
sch_hour = np.asarray(sc_hour['hour'])
sch_load = np.asarray(sc_hour['scaledload'])

sc_month = pd.read_csv('scaledMonthLoad.csv')
scm_month = np.asarray(sc_month['month'])
scm_load = np.asarray(sc_month['scaledload'])

sc_week = pd.read_csv('scaledWeekLoad.csv')
scw_day = np.asarray(sc_week['day'])
scw_load = np.asarray(sc_week['scaledload'])

size_data = len(fd_load)
day_counter = 0
mon_counter = 0

with open('mergedData.csv','w') as myFile:
    writer = csv.writer(myFile)
    writer.writerows([['date','hour','day','month','load','shr_load','sday_load',
                       'smon_load','prevload','temp','humid','windspd']])
    for i in range(size_data):
        var_day = fd_day[i]
        var_hour = fd_hour[i]
        var_month = fd_month[i]
        var_load = fd_load[i]
        var_date = fd_date[i]

        vsh_hour = sch_hour[i]
        vsh_load = sch_load[i]

        vsd_day = scw_day[day_counter]
        vsm_month = scm_month[mon_counter]

        if var_day != vsd_day:
            day_counter += 1
        if var_month != vsm_month:
            mon_counter += 1

        vsd_load = scw_load[day_counter]
        vsm_load = scm_load[mon_counter]

        writer.writerows([[var_date,var_hour,var_day,var_month,var_load,vsh_load,vsd_load,
                           vsm_load,fd_prevload[i],fd_temp[i],fd_humid[i],fd_windspd[i]]])
