from pymongo import MongoClient
from bson import Binary
import datetime

class FetchData:

    def __init__(self,url):
        self.client = MongoClient(host=url)

    def getTrainData(self,zone):
        db = self.client.zones
        val = {'temp':[],'date':[],'hour':[],'month':[],'weekday':[],'load':[],'prevload':[],'lasthr':[]}
        curs=db['zone'+str(zone)].find()
        for doc in curs:
            val['temp'].append(doc['temp'])
            val['hour'].append(doc['hour'])
            val['weekday'].append(doc['weekday'])
            val['load'].append(doc['load'])
            val['date'].append(doc['date'])
            val['month'].append(doc['month'])
            val['prevload'].append(doc['prevload'])
            val['lasthr'].append(doc['lasthr'])
        return val

    def get_obj(self,name,zone):
        oid = str(name)
        db = self.client.picklestore
        col = db['zone' + str(zone)]
        dic = col.find({'_id':oid})
        dic = list(dic)
        return dic[0]['obj'],dic[0]['preprocessing'],dic[0]['PCA']

    def storeObj(self, pickleobj, zone, acc, preobj,pca , name='{0}/{1}/{2}{3}'.format(datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year, datetime.datetime.now().hour)):
        db = self.client.picklestore
        col = db['zone' + str(zone)]
        dic = {'_id': name, 'obj': Binary(pickleobj), 'accuracy': acc,'preprocessing':preobj,'zone':zone,'PCA':pca}
        col.insert(dic)

    def setCurrentObj(self, obj, zone, name,preobj,pca,acc):
        db = self.client.picklestore
        col = db['currentWrkObj']
        col.update({'_id': zone}, {'$set': {'_id': zone, 'obj': Binary(obj), 'name': name,'preprocessing':preobj,'PCA':pca,'accuracy':acc}}, upsert=True)

    def get_current_obj(self,zone):
        db = self.client.picklestore
        col = db['currentWrkObj']
        val = list(col.find({'_id': zone}))
        return val[0]['obj'],val[0]['preprocessing'],val[0]['PCA']


    def predictstore(self,id,pred_load,actual_load,zone):
        load_dict = {'_id': id, 'actual_load': actual_load, 'pred_load': pred_load}
        db = self.client.prediction
        col =db['zone{}'.format(zone)]
        col.insert_one(load_dict)


    def gettestdata(self,dataid,zone):
        db = self.client.tests
        ls = list(db['zone{}'.format(zone)].find({'_id':dataid}).sort([('$natural', -1)]).limit(1))
        return ls[0]

    def __del__(self):
        self.client.close()

if __name__ == '__main__':
    print (FetchData.gettestdata(FetchData('192.168.0.173'),'1/1/20081',1))