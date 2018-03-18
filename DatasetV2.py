from pymongo import MongoClient
from urllib2 import urlopen
from bson import json_util as jso
from json import loads


url="http://api.wunderground.com/api/85053054493a69d0/history_20101010/q/CA/Mumbai.json"
dat=urlopen(url)
js = loads(dat.read())
for x in js['history']['observations']:
    print x['tempm'], x['hum'], x['wspdm'],x['date']['hour']


