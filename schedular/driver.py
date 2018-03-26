from utils.function_schedular import FunSch
import os,signal
import datetime
import time
def driver(id,num):

    print "process created: ",time.time(),num,id



FunSch.pediction_start_next_hour((driver,50))
print  "hello"
# arr = []
#
# for m in range(1,7):
#     if m in [1,3,5,7]:
#         days = range(1,32)
#     if m in [4,6]:
#         days = range(1,31)
#     if m in [2]:
#         days = range(1,29)
#     for d in days:
#         for h in range(1,25):
#             if d == 30 and m == 6 and h>=7:
#                 continue
#             _id = '{0}/{1}/2008{2}'.format(d,m,h)
#             arr.append(_id)
#
# print len(arr),arr[4325]
# # 4344