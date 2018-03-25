from pymongo import MongoClient

client = MongoClient(host='192.168.0.230')
db = client.zones


def getTrainData(zone):
    val = {'temp':[],'date':[],'hour':[],'month':[],'weekday':[],'load':[]}
    curs=db['zone'+str(zone)].find()
    for doc in curs:
        val['temp'].append(doc['temp'])
        val['hour'].append(doc['hour'])
        val['weekday'].append(doc['weekday'])
        val['load'].append(doc['load'])
        val['date'].append(doc['date'])
        val['month'].append(doc['month'])
    return val

print getTrainData(1)