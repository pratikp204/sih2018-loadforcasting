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
    def _Job(fun_tup):
        def job():
            fun_tup[0](fun_tup[1])
        nextHr = FunSch.roundTime(datetime.datetime.now(),roundTo=3600)
        nextHr += datetime.timedelta(days=1)
        time.sleep((nextHr - datetime.datetime.now()).seconds)
        schedule.every(1).minute.do(job)
        job()
        while True:
            schedule.run_pending()
            time.sleep(1)

    def info(self,title):
        print title
        print 'module name: ', __name__
        if hasattr(os, 'getppid'):
            print 'parent process:', os.getppid()
        print 'process id:', os.getpid()

    @staticmethod
    def startNextHour(fun_tup):
        p = multiprocessing.Process(target= FunSch._Job,args=(fun_tup,))
        p.start()
        p.join()

    def print_pid(self):
        print self.pid

    def kill_schedular(self,name):
        os.kill(self.pid[name],signal.SIGTERM)