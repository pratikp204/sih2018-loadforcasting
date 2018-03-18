import pandas as pd
df = pd.read_csv('Constructed dataset.csv')
df1 = pd.read_csv('dataWeather.csv')
df['temp'] = df1['temp']
df['humid'] = df1['humid']
df['windspd'] = df1['windspd']
print df
f=open('finaldataset.csv','wb')
pd.DataFrame.to_csv(df,path_or_buf=f,index=False,columns=['monthofyear','dayofmonth','Date','Hour','load','prevload','temp','humid','windspd'])