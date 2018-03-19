import pandas as pd
from urllib2 import urlopen
from json import loads
import datetime


def hourly():
    url = "http://api.wunderground.com/api/85053054493a69d0/hourly/q/CA/Mumbai.json"
    dat = urlopen(url)
    js = loads(dat.read())
    for x in js['hourly_forecast']:
        if x['FCTTIME']['hour_padded']==str(datetime.datetime.now().hour+1):
            return {'temp':x['temp']['metric'],'windspd':x['wspd']['metric'],'humid': x['humidity']}


def batch_step(n_size):
    x= 0
    dfl=[]
    n_size1=n_size
    df = pd.read_csv('Constructed dataset.csv')
    for z in range(0,(len(df)/n_size)):
        dfl.append(df.loc[x:n_size1-1])
        x=x+n_size
        n_size1+=n_size
    if len(df)%n_size!=0:
        dfl.append(df.loc[x:])
    return dfl
