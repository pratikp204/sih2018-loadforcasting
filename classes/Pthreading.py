import threading
from classes.FetchDataUnit import FetchData
from classes.Regression import Regression
import schedule,time,datetime

class Pthreading(threading.Thread):

    def __init__(self,zone,host):
        super(Pthreading,self).__init__()
        self.__stop_event = threading.Event()
        self.val = 0
        self.zone = zone
        self.host = host

    def roundTime(self,dt, roundTo=60):
        seconds = (dt.replace(tzinfo=None) - dt.min).seconds
        rounding = (seconds + roundTo) // roundTo * roundTo
        return dt + datetime.timedelta(0, rounding - seconds, -dt.microsecond)

    def run(self):
        print 'thread {} alive'.format(self.zone)
        arr = []
        prd_arr = []
        for m in range(1, 7):

            if m in [1, 3, 5, 7]:
                days = range(1, 32)
            if m in [4, 6]:
                days = range(1, 31)
            if m in [2]:
                days = range(1, 29)
            for d in days:

                for h in range(1, 25):
                    # if m == 1 and d<15 and h <17:
                    #     continue
                    if m == 6 and d == 30 and h > 6:
                        continue
                    _id = '{0}/{1}/2008{2}'.format(d, m, h)
                    pred_id = '{0}/{1}/2008/{2}'.format(d, m, h-1)
                    arr.append(_id)
                    prd_arr.append(pred_id)

        def job():

            fd = FetchData(self.host)
            a =FetchData.gettestdata(fd,arr[self.val],self.zone)
            pred_load= Regression.predict(a,'first test',self.zone,self.host)
            FetchData.predictstore(fd,prd_arr[self.val],pred_load[0],a['load'],self.zone)

            print prd_arr[self.val],a['load'],pred_load[0],self.zone
            self.val += 1

        nextHr = self.roundTime(datetime.datetime.now(), roundTo=60)
        nextHr += datetime.timedelta(days=1)
        # time.sleep((nextHr - datetime.datetime.now()).seconds)

        schedule.every(5).seconds.do(job)
        job()
        while True:
            if self.val == 4326:
                break
            schedule.run_pending()
            time.sleep(1)




if __name__ == '__main__':
    p = Pthreading(1,'192.168.43.91')
    p.start()
    p.join()
    print 'done'