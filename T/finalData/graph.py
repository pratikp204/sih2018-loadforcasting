from utils import Graph_gen
import pandas as pd
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np

for itr in range(1,11):
    print "into {}".format(itr)
    df = pd.read_csv('T{}_train.csv'.format(itr))
    figName = 'graphs/T{}_hourVmeanLoad'.format(itr)
    YrefList = df['hour']
    listY = df['load']

    # plt.scatter(YrefList,listY)
    # plt.xlabel('temperature')
    # plt.ylabel('load')
    # plt.legend()
    # plt.savefig(figName)
    # plt.close()
    # plt.show()
    Graph_gen.graph_generator(range(1,25),listY,YrefList,(1,25),xlabel='hour',ylabel='mean load',svfig=figName,showgraph=False)
    print "out"
