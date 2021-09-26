import csv
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.animation import FuncAnimation
import numpy as np
import math

#Starting with empty arrays for the data
x_values = []
y_values = []

#Making the figure produce 2 subplots (graphs)
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
fig.set_size_inches(12, 7)

#Initialisation of packet counters
TotalPacketCountG1 = fig.text(0.81, 0.82,'')
TotalRedCountG1 = fig.text(0.81, 0.77,'')
TotalOrangeCountG1 = fig.text(0.81, 0.72,'')
TotalGreenCountG1 = fig.text(0.81, 0.67,'')
RedPercentageG1 = fig.text(0.81, 0.53,'')

TotalPacketCountG2 = fig.text(0.81, 0.40,'')
TotalRedCountG2 = fig.text(0.81, 0.35,'')
TotalOrangeCountG2 = fig.text(0.81, 0.30,'')
TotalGreenCountG2 = fig.text(0.81, 0.25,'')
RedPercentageG2 = fig.text(0.81, 0.08,'')

def livedata(i):
   
    #Reading the data from the generated csv files
    gooddata = pd.read_csv('data1.csv')
    baddata = pd.read_csv('data2.csv')

    #Selecting the columns from the CSV files by name
    a = gooddata['packet_identifier']
    b = gooddata['ttl_value']
    x = baddata['packet_identifier']
    y = baddata['ttl_value']
    
    #Clearing the subplots every iteration so the graph can be created again with the newest data
    ax1.cla()
    ax2.cla()

    #Initialisation of the counting variables
    graphOneCount = 0
    graphOneRedCount = 0
    graphTwoRedCount = 0
    graphOneOrangeCount = 0
    graphTwoOrangeCount = 0
    graphOneGreenCount = 0
    graphTwoGreenCount = 0
    
    #Top Graph (graph one)
    for i in b:
        if i >= 250: 
            ax1.scatter(graphOneCount, i, color='#FF0000') #mark packet as red (dangerous)
            graphOneRedCount+=1
        elif i <= 249 and i > 200:
            ax1.scatter(graphOneCount, i, color='#FFC158') #mark packet as orange (could be dangerous)
            graphOneOrangeCount+=1
        else:
            ax1.scatter(graphOneCount, i, color='#1EDB2C') #mark as green (packet is fine for now)
            graphOneGreenCount+=1
        graphOneCount+=1

    graphTwoCount = 0

    #Bottom Graph (graph two)
    for j in y:
        if j >= 250:
            ax2.scatter(graphTwoCount, j, color='#FF0000') #mark packet as red (dangerous)
            graphTwoRedCount+=1
        elif j <= 249 and j > 200:
            ax2.scatter(graphTwoCount, j, color='#FFC158') #mark packet as orange (could be dangerous)
            graphTwoOrangeCount+=1
        else:
            ax2.scatter(graphTwoCount, j, color='#1EDB2C') #mark as green (packet is fine for now)
            graphTwoGreenCount+=1
        graphTwoCount+=1

    #Setting the axis labels
    ax1.set_title("TTL packet values")
    ax1.set_ylabel("TTL Value")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("TTL Value")

    #Graph one packet counters
    TotalPacketCountG1.set_position([0.81, 0.82])
    TotalPacketCountG1.set_text('Packet count: '+ str(graphOneCount))

    TotalRedCountG1.set_position([0.81, 0.77])
    TotalRedCountG1.set_text('Red packets: '+ str(graphOneRedCount))

    TotalOrangeCountG1.set_position([0.81, 0.72])
    TotalOrangeCountG1.set_text('Orange packets: '+ str(graphOneOrangeCount))

    TotalGreenCountG1.set_position([0.81, 0.67])
    TotalGreenCountG1.set_text('Green packets: '+ str(graphOneGreenCount))

    RedPercentageG1.set_position([0.81, 0.53])
    RedPercentageG1.set_text('Percent of red packets: '+str(round((graphOneRedCount/graphOneCount)*100)) + '%')

    #Graph two packet counters
    TotalPacketCountG2.set_position([0.81, 0.40])
    TotalPacketCountG2.set_text('Packet count: '+ str(graphTwoCount))

    TotalRedCountG2.set_position([0.81, 0.35])
    TotalRedCountG2.set_text('Red packets: '+ str(graphTwoRedCount))

    TotalOrangeCountG2.set_position([0.81, 0.30])
    TotalOrangeCountG2.set_text('Orange packets: '+ str(graphTwoOrangeCount))

    TotalGreenCountG2.set_position([0.81, 0.25])
    TotalGreenCountG2.set_text('Green packets: '+ str(graphTwoGreenCount))

    RedPercentageG2.set_position([0.81, 0.08])
    RedPercentageG2.set_text('Percent of red packets: '+str(round((graphTwoRedCount/graphTwoCount)*100)) + '%')

#Function to plot the live data
livedataplotter = FuncAnimation(plt.gcf(), livedata, interval=1000)

#Adjusting the right side padding of the graph
plt.subplots_adjust(right=0.8)
plt.show()