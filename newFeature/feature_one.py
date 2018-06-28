import pandas as pd
import numpy as np
from statistics import mean

df = pd.read_csv('T1_train.csv')

load = np.asarray(df['load'])
hr = np.asarray(df['hour'])

vlist = {}
for x in range(24):
    vlist[x]=[]
x = 0
for i in range(5*24):
    vlist[x].append(load[i])
    x = (x+1)%24
global V
V = [[] for i in range(24)]
for i in range(24):
    lis = vlist[i]
    V[0].append(mean(lis))
    vlist[i] =[]
x = 0
for i in range(120,len(load)):
    vlist[x].append(load[i])
    x = (x+1)%24


c0 = 0.1    # alpha
c1 = 0.9    # 1 - alpha
# global counter
counter = len(vlist[0])
def function(counter,theta_n):
    x = len(theta_n)
    c0theta = c0 * theta_n.pop()

    num = c0theta + (c1* function(counter+1,theta_n))

function()