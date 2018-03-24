import matplotlib.pyplot as plt
from statistics import  mean
import pandas as pd
from graphGenerator import graph_generator

df = pd.read_csv('Constructed datasetV2.csv')

hours = df['Hour']
ld = df['load']
loads = []
loads.append(0)
for i in range(1,len(ld)):
    loads.append(ld[i]-ld[i-1])
graph_generator(range(1,25),loads,hours,(1,25))

#
# hourload = {}
# for i in range(1,25):
#     hourload[i] = []
# for i in range(len(hours)):
#     hourload[hours[i]].append(loads[i])
# avg_load = []
#
# for i in range(1,25):
#     avg_load.append(mean(hourload[i]))
#
# plt.plot(range(1,25),avg_load)
# plt.legend()
# plt.show()