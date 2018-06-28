from pymongo import MongoClient
import pandas as pd
con = MongoClient(host='192.168.43.91')
for i in range(1,11):
    v='zone'+str(i)
    print v
    db=con['tests_v2']
    df = pd.read_csv('T'+str(i)+'_test.csv')
    dataf = pd.read_csv('vntest{}.csv'.format(i))
    dataf = dataf.reset_index(drop=True)
    # print dataf['feature'][4224]
    print len(dataf)
    val = {}
    x=0
    counter=0
    for z in range(0,len(df)):
        ls = list(con['test_zones'][v].find().sort([('$natural',-1)]).limit(1))
        val['temp']=float(df['temp'][z])
        val['hour']=int(df['hour'][z])
        val['weekday']=int(df['weekday'][z])
        val['load']=float(df['load'][z])
        val['date']=str(df['date'][z])
        val['month']=int(df['month'][z])

        val['lasthr']=float(ls[0]['load'])
        val['_id'] = str(val['date'])+str(val['hour'])
        # con['test_zones'][v].insert(val,{'ordered':True})
        if z < 120:
            val['prevload'] = dataf['feature'][x].astype(float)
            x = (x + 1) % 24
        else:
            val['prevload'] = dataf['feature'][counter].astype(float)
            counter += 1
        db[v].insert(val)
    print 'inserted',i
