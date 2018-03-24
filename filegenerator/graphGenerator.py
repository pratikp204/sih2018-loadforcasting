from statistics import mean
import pandas as pd
import matplotlib.pyplot as plt
def graph_generator(listX,listY,YrefList,rtup):

    totListY = {}
    for i in range(rtup[0],rtup[1]):
        totListY[i] = []
    for i in range(len(listY)):
        totListY[YrefList[i]].append(listY[i])

    avg_load = []

    for i in range(rtup[0],rtup[1]):
        avg_load.append(mean(totListY[i]))

    plt.plot(listX, avg_load)
    plt.legend()
    plt.show()