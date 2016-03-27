# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 02:31:25 2016

@author: Anton
"""

import numpy as np, math, random, matplotlib, matplotlib.pyplot as plt
plt.style.use('ggplot')

from pandas.io.data import DataReader
from datetime import datetime




historical_stock = DataReader('BIIB',  'yahoo', datetime(2010,1,1), datetime(2016,1,1))
print(historical_stock['Adj Close'])

Mean = 0 #Mu value in order to get a drift
Sigma = 0 #Sigma value in order to get a drift
Dt = 1/float(252) #Delta Time = 1 over 252 trading days. -> One trading day
P0=0 #Price @ Time0
Return=[] #Returns




sample_size=len(historical_stock['Adj Close']) #sample size
i=0 #itterator
while i<sample_size-1:
    st_0=historical_stock.irow(i)['Adj Close']
    st_1=historical_stock.irow(i+1)['Adj Close']
    Return.append(math.log(float(st_1)/float(st_0)))
    i+=1

Mean = np.average(Return)#Setting up Mu value
Sigma = np.std(Return)#Setting up Sigma value
P0=historical_stock.irow(len(historical_stock['Adj Close'])-1)['Adj Close']
xD0=[]
yS0=[]   
    
plt.plot(historical_stock[1258:1510:1]['Adj Close'])


def MonteCarlo(p0, mean, sigma, dt, p):
    xD=[]
    yS=[]
    ps=p0
    t=len(p[1258:1510:1]['Adj Close'])
    print(t)
    cap=t+(100)
        
    while t<cap:
        ps = math.exp(math.log(ps)+random.normalvariate(Mean, Sigma))
        t+=1
        yS.append(ps)
        xD.append(t)
    plt.plot(xD,yS)
    
    
x=1
while x<100:
    MonteCarlo(P0, Mean, Sigma, Dt, historical_stock)
    x+=1

