import multiprocessing,datetime, time, schedule,os,signal


class FunSch():

    def __init__(self):
        self.pid = None
        return

    @staticmethod
    def roundTime(dt, roundTo=60):
        seconds = (dt.replace(tzinfo=None) - dt.min).seconds
        rounding = (seconds + roundTo) // roundTo * roundTo
        return dt + datetime.timedelta(0, rounding - seconds, -dt.microsecond)

    @staticmethod
    def _Job(fun_tup,val,lock):
        arr = []
        for m in range(1, 7):
            if m in [1, 3, 5, 7]:
                days = range(1, 32)
            if m in [4, 6]:
                days = range(1, 31)
            if m in [2]:
                days = range(1, 29)
            for d in days:
                for h in range(1, 25):
                    if m == 6 and d == 30 and h > 6:
                        continue
                    _id = '{0}/{1}/2008{2}'.format(d, m, h)
                    arr.append(_id)
        def job():
            if val.value == 4326:
                exit(0)
            fun_tup[0](fun_tup[1],arr[val.value])
            with lock:
                val.value += 1
            # fun_tup[0](fun_tup[1][0],fun_tup[1][1],fun_tup[1][2])

        nextHr = FunSch.roundTime(datetime.datetime.now(),roundTo=60)
        nextHr += datetime.timedelta(days=1)
        time.sleep((nextHr - datetime.datetime.now()).seconds)
        schedule.every(1).minute.do(job)
        job()
        while True:
            schedule.run_pending()
            time.sleep(1)

    @staticmethod
    def pediction_start_next_hour(fun_tup):
        v = multiprocessing.Value('i',0)
        lock = multiprocessing.Lock()
        p = multiprocessing.Process(target= FunSch._Job,args=(fun_tup,v,lock,))
        p.start()
        p.join()

    def info(self, title):
        print title
        print 'module name: ', __name__
        if hasattr(os, 'getppid'):
            print 'parent process:', os.getppid()
        print 'process id:', os.getpid()

    def print_pid(self):
        print self.pid

    def kill_schedular(self,name):
        os.kill(self.pid[name],signal.SIGTERM)