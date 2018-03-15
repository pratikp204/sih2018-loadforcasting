from urllib2 import urlopen
from bs4 import BeautifulSoup
import json
from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.weather
def make_soup(url):
    page = urlopen(url)
    soupdata = BeautifulSoup(page, "html.parser")
    return soupdata
main_dict={}
di={"temp":"","humidity":"","windspd":""}
zone = {}
varTemp=0
varWindspd=0
varHumid=0
varTime=0
yr=[2015,2016,2017]
mon=range(1,13)
for yy in yr:
    zone[yy]={}
    for m in mon:
        zone[yy][m] = {}
        if m in[1,3,5,7,8,10,12]:
            day=range(1,32)
        if m in[4,6,9,11]:
            day=range(1,31)
        if m in[2]:
            if yy%4==0:
                day=range(1,30)
            else:
                day=range(1,29)
        for y in day:
            zone[yy][m][y] = {}
            dat=str(yy)+"/"+str(m)+"/"+str(y)
            print dat
            zone[yy][m][y]["date"]=dat
            zone[yy][m][y]["value"] = []
            url="https://www.wunderground.com/history/airport/VABB/{0}/{1}/{2}/DailyHistory.html".format(yy,m,y)
            soup = make_soup(url)
            for record in soup.find_all('table', {'id': 'obsTable'}):
                for data in record.find_all('tr'):
                    b = 0
                    for x in data.find_all('td'):
                        if b in [0]:
                            # di["time"].append(x.text)
                            varTime= x.text
                        if b in [1]:
                            if x.find_all("span"):
                                for tem in x.find_all("span")[1]:
                                    # di["temp"].append(tem)
                                    varTemp = tem
                            else:
                                # di["temp"].append(0)
                                varTemp = 0
                        if b in [4]:
                            varHumid=x.text
                            # di["humidity"].append(x.text)
                        if b in [8]:
                            if x.text =="Calm":
                                # di["windspd"].append(x.text)
                                varWindspd=x.text
                                continue
                            ch=True
                            for tem in x.find_all("span"):
                                for temp in tem.find_all("span",{"class":"wx-value"}):
                                   if ch==True:
                                        # di["windspd"].append(temp.text)
                                        varWindspd=temp.text
                                        ch=False
                        b += 1
                    zone[yy][m][y]["value"].append({"time": varTime, "temp": varTemp,"humidity":varHumid,"windspd":varWindspd})
            # main_dict[dat]=di
            # di={"time":[],"temp":[],"humidity":[],"windspd":[]}


jsonobj=json.dumps(zone)

db.mumbaiOne.insert(json.loads(jsonobj))