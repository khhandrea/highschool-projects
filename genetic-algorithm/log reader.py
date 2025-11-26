import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


def plot():
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    pullData = open("gene log.txt", "r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.set_xlabel('generations')
    ax1.set_ylabel('evaluation')
    ax1.plot(xar, yar)
    plt.show()
