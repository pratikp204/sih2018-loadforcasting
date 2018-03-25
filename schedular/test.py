import schedule, multiprocessing, time,datetime

def roundTime(dt=None, roundTo=60):

   if dt == None : dt = datetime.datetime.now()
   seconds = (dt.replace(tzinfo=None) - dt.min).seconds
   rounding = (seconds+roundTo) // roundTo * roundTo
   return dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)

def spawn(num):
    print "Spawned! {}".format(num)

def job():
    p = multiprocessing.Process(target=spawn,args=(time.time(),))
    p.start()
    p.join()

va =roundTime()
t = datetime.datetime.today()
va += datetime.timedelta(days=1)
print  va
sec = (va-t).seconds
print sec
time.sleep(sec)
schedule.every(2).seconds.do(job)

print( 'hello')
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)