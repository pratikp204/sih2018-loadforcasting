import pandas as pd
import arrow
import datetime

df = pd.read_csv('temperature_history.csv')
# df1 = pd.read_csv('Load_history.csv')
# i=0
# for z in range(1,11):
#     dat = []
#     hrs = []
#     wd = []
#     hr = []
#     mon = []
#     d = []
#     zid = []
#     while df1['zone_id'][i] == z:
#         for x in range(1,25):
#             zid.append(df1['zone_id'][i])
#             dt = str(str(df1['day'][i]) + '/' + str(df1['month'][i]) + '/' + str(df1['year'][i]))
#             d.append(df1['day'][i])
#             mon.append(df1['month'][i])
#             hr.append(x)
#             dat.append(dt)
#             hrs.append(df1['h' + str(x)][i])
#             wd.append(datetime.datetime.fromtimestamp(
#                 arrow.get(datetime.datetime.strptime(dt, "%d/%m/%Y")).timestamp).weekday() + 1)
#         i+=1
#     pdf = pd.DataFrame({'date': dat, 'weekday': wd, 'day': d, 'month': mon, 'load': hrs, 'hour': hr, 'zone': zid})
#     pd.DataFrame.to_csv(pdf[:39415], path_or_buf='v'+str(z)+'.csv', index=False)
i=0
for z in range(1,11):
    dat = []
    hrs = []
    zid = []
    while df['station_id'][i] == z:
        for x in range(1,25):
            hrs.append(df['h' + str(x)][i])
        i+=1
    pdf = pd.read_csv('v'+str(z)+'.csv')
    pdf['Temp'] = hrs[:39415]
    pd.DataFrame.to_csv(pdf, path_or_buf='T'+str(z)+'.csv', index=False)
