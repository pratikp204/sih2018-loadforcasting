from utils import Graph_gen
import pandas as pd
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np

for itr in range(1,11):
    print "into {}".format(itr)
    df = pd.read_csv('T{}_train.csv'.format(itr))
    figName = 'T{}_tempVLoad'.format(itr)
    YrefList = df['Temp']
    listY = df['load']

    plt.scatter(YrefList,listY)
    plt.xlabel('temperature')
    plt.ylabel('load')
    plt.legend()
    # plt.savefig(figName)
    plt.show()
    # Graph_gen.graph_generator(range(1,13),listY,YrefList,(1,13),xlabel='month',ylabel='mean load',svfig=figName)
    print "out"
