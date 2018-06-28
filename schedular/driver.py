# for m in range(1, 7):
#     if m in [1, 3, 5, 7]:
#         days = range(1, 32)
#     if m in [4, 6]:
#         days = range(1, 31)
#     if m in [2]:
#         days = range(1, 29)
#     for d in days:
#         if m == 1 and d  <14:
#             continue
#         for h in range(1, 25):
#             if m == 1 and d<15 and h <12:
#                 continue
#             if m == 6 and d == 30 and h > 6:
#                 continue
#             print '{}/{}/2008{}'.format(d, m, h)

from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2013, 1, 1)
end_date = date(2015, 6, 2)
for single_date in daterange(start_date, end_date):
    print single_date.strftime("%Y-%m-%d")
