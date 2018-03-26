import multiprocessing,datetime, time, schedule,os

class FunSch():

    def __init__(self):
        return

    @staticmethod
    def roundTime(dt, roundTo=60):
        seconds = (dt.replace(tzinfo=None) - dt.min).seconds
        rounding = (seconds + roundTo) // roundTo * roundTo
        return dt + datetime.timedelta(0, rounding - seconds, -dt.microsecond)

    def _Job(self):
        def job():
            self.info('inside function to be scheduled')
            self.fun_name(self.fun_arg)
        self.info('inside _Job function')
        nextHr = FunSch.roundTime(datetime.datetime.now(),roundTo=self.duration)
        nextHr += datetime.timedelta(days=1)
        time.sleep((nextHr - datetime.datetime.now()).seconds)
        schedule.every(1).hours.do(job)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def info(self,title):
        print title
        print 'module name: ', __name__
        if hasattr(os, 'getppid'):
            print 'parent process:', os.getppid()
        print 'process id:', os.getpid()

    def startNextHour(self,fun_name,fun_arg):
        self.duration =3600
        self.fun_name = fun_name
        self.fun_arg = fun_arg
        p = multiprocessing.Process(target= self._Job)
        p.start()
