from FunSch import FunSch
import time
def driver(num):
    print "process created: ",num


funOb = FunSch()
funOb.info('driver')
funOb.startNextHour(driver,(time.time()))