from pymongo import MongoClient
from bson import Binary
import datetime
client = MongoClient(host='192.168.0.230')
db = client.zones


class FetchDataUnit:

    def getTrainData(self,zone):
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

    def storeData(self,pickleobj,zone,accuracy,model):
        da = datetime.datetime.now()
        db = client.picklestore
        col = db['zone'+str(zone)]
        dic = {'_id':'{0}{1}{2}{3}'.format(da.day,da.month,da.year,da.hour),'obj':Binary(pickleobj),'accuracy':accuracy,'model':model}
        col.insert(dic)

    def get_obj(self,date,zone):
        oid = str(date).replace('/','')
        db = client.picklestore
        col = db['zone' + str(zone)]
        dic = col.find({'_id':oid})
        return dic['obj']

if __name__ == '__main__':
    s = FetchDataUnit()
