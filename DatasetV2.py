from pymongo import MongoClient
from urllib2 import urlopen
from bson import json_util as jso
from json import loads
from json import dumps
import csv



client = MongoClient('localhost',27018)
db = client['mumbaiTwo']
with open('dataWeather.csv','w') as myFile:
    writer = csv.writer(myFile)
    writer.writerows([['date','time','temp','humid','windspd']])

    for year in range(2010,2015):
        yearString = 'y'+str (year)
        collection = db[yearString]
        for month in range(1,13):
            if month in[1,3,5,7,8,10,12]:
                days=range(1,32)
            if month in[4,6,9,11]:
                days=range(1,31)
            if month in [2]:
                if year % 4 ==0:
                    days = range(1,30)
                else:
                    days = range(1,29)
            for day in days:
                if day < 10:
                    dayString = '0' + str(day)
                else:dayString = str(day)
                if month < 10:
                    monthString = '0'+str(month)
                else:monthString = str(day)
                dateUrl = str(year)+monthString+dayString
                url="http://api.wunderground.com/api/85053054493a69d0/history_{0}/q/CA/Mumbai.json".format(dateUrl)
                dateToday = str(day)+'/'+str(month)+'/'+str(year)
                dat=urlopen(url)

                js = loads(dat.read())

                temperature = [0.]*24
                humidity = [0.]*24
                windSpeed = [0.]*24
                counter = [0.]*24

                for x in js['history']['observations']:
                    index = int(x['date']['hour'])
                    try:
                        temperature[index] += float(x['tempm'])
                        humidity[index] += float(x['hum'])
                        windSpeed[index] += float(x['wspdm'])
                        counter[index] += 1
                    except:
                        print "error: ",x['tempm']
                for i in range(24):
                    if counter[i] == 0 :
                        # temperature[i]=temperature[i-1]
                        # humidity[i]=humidity[i-1]
                        continue
                    temperature[i] =format((temperature[i]/counter[i]),'.2f')
                    humidity[i] =format((humidity[i]/counter[i]),'.2f')
                    windSpeed[i] =format((windSpeed[i]/counter[i]),'.2f')
                print dateUrl
                for i in range(24):
                    writer.writerows([[dateToday,i+1,temperature[i],humidity[i],windSpeed[i]]])
                dataDict = {'date':dateToday,'temp':temperature,'humidity':humidity,'windspeed':windSpeed}
                collection.insert(dataDict)
# print temperature
# print humidity
# print windSpeed