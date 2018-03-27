from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from classes import CentralProcessor

class Graph_gen():

    @staticmethod
    def graph_generator(listX,listY,YrefList,rtup,xlabel="x-axis",ylabel='y-axis',svfig=None,showgraph=True):

        totListY = {}
        for i in range(rtup[0],rtup[1]):
            totListY[i] = []
        for i in range(len(listY)):
            totListY[YrefList[i]].append(listY[i])

        avg_load = []

        for i in range(rtup[0],rtup[1]):
            avg_load.append(np.nanmean(totListY[i]))

        plt.plot(listX, avg_load)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        if svfig!=None:
            plt.savefig(svfig+".png")
        if showgraph:
            plt.show()
        plt.close()
if __name__=='__main__':
    CentralProcessor.periodic_prediction_schedular(1)