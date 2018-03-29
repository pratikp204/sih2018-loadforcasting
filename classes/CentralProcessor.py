from Regression import Regression
from FetchDataUnit import FetchData
import multiprocessing,datetime,schedule,time
from threading import Thread

class CentralProcessor():

    def __init__(self,curent_timestamp,default_api_code,last_schedules):
        self.curent_timestamp = curent_timestamp
        self.default_api_code = default_api_code
        self.last_schedules = last_schedules

    @staticmethod
    def zone_periodic_prediction(zone,port='192.168.0.173'):
        v = multiprocessing.Value('i', 0)
        lock = multiprocessing.Lock()
        p = multiprocessing.Process(target=CentralProcessor._Job, args=(zone, v, lock,port,))
        p.start()
        p.join()

    @staticmethod
    def periodic_prediction_schedular():
        v = multiprocessing.Array('i',)
        lock = multiprocessing.Lock()
        p = multiprocessing.Process(target=CentralProcessor._Job, args=(zone, v, lock, port,))
        p.start()
        p.join()

    def periodic_training_schedular(self):
        pass

    def save_training_module(self):
        pass

    def load_regressor(self):
        pass

    def predict(self):
        pass

    def schedule_training(self):
        pass

    @staticmethod
    def run_ten_prediction( v, lock, port):
        for i in range(1,11):
            t = Thread(target=CentralProcessor._Job, args=(i,v,lock,port,))
            t.start()
    @staticmethod
    def roundTime(dt, roundTo=60):
        seconds = (dt.replace(tzinfo=None) - dt.min).seconds
        rounding = (seconds + roundTo) // roundTo * roundTo
        return dt + datetime.timedelta(0, rounding - seconds, -dt.microsecond)

    @staticmethod
    def _Job(zone, val, lock,host):
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
                # if m == 1 and d<14:
                #     continue
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
            if val.value == 4326:
                exit(0)

            a =FetchData.gettestdata(FetchData(host),arr[val.value],zone)
            pred_load= Regression.predict(a,'first test',zone,host)
            FetchData.predictstore(FetchData(host),prd_arr[val.value],pred_load[0],a['load'],zone)
            print prd_arr[val.value]
            with lock:
                val.value += 1
        nextHr = CentralProcessor.roundTime(datetime.datetime.now(), roundTo=60)
        nextHr += datetime.timedelta(days=1)
        time.sleep((nextHr - datetime.datetime.now()).seconds)

        schedule.every(1).seconds.do(job)
        job()
        while True:
            schedule.run_pending()
            time.sleep(1)



if __name__== '__main__':
    CentralProcessor.periodic_prediction_schedular(4)