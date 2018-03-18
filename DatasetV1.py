from dateutil.parser import parser as pas
import datetime
import arrow
import pandas as pd
df = pd.read_csv("GEFCom2014-E.csv",date_parser="%d/%m/%y",keep_date_col='Date')
da,mo,wd=[],[],[]
dates=list(df['Date'])
df['prevload'] = df.load.shift(24)
for x in dates:
    d,m,y=x.split('/')
    da.append(d)
    mo.append(m)
    wd.append(datetime.datetime.fromtimestamp(arrow.get(datetime.datetime.strptime(x,"%d/%m/%Y")).timestamp).weekday()+1)

df['dayofmonth'] = da
df['monthofyear'] = mo
df['weekday'] = wd
f=open("Constructed dataset.csv",'w')
pd.DataFrame.to_csv(df,path_or_buf=f,columns=['monthofyear','dayofmonth','weekday','Date','Hour','load','prevload'],index=False)
