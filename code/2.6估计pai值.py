import random
import numpy as np
from typing import Counter
def throwNeedles(numNeedles):
    incircle = 0
    for Needles in range(1,numNeedles+1):
        x = random.random()
        y = random.random()
        if (x*x+y*y)**0.5<=1:
            incircle+=1
    return 4*(incircle/numNeedles)

def stddev(estimates):
    mean = np.std(estimates,ddof=1)
    return mean

def getEst(numNeedles,numTrials):
    estimates = []
    for t in range(numTrials):
        piguess = throwNeedles(numNeedles)
        estimates.append(piguess)
    sdev = stddev(estimates)
    curEst = sum(estimates)/len(estimates)
    print('Est=',str(round(curEst,5))+',','Std.dev.=',str(round(sdev,5))+',','Needles=',numNeedles)
    return curEst,sdev

def estPi(precision,numTrials):
    numNeedles = 1000
    sdev = precision
    while sdev > precision/1.96:
        curEst,sdev = getEst(numNeedles,numTrials)
        numNeedles *= 2
    return curEst

def main():
    estPi(0.001,1000)

if __name__ == '__main__':
    main()