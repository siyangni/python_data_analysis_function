# Write a function to perform Cronbach's Alpha Calculation 
# Forked from Github: https://gist.github.com/lauramar6261/7b6b3ede3cb5f7e23c75f0a93ffb869e

import numpy as np

def svar(X):
    n = float(len(X))
    svar=(sum([(x-np.mean(X))**2 for x in X]) / n)* n/(n-1.)
    return svar

def CronbachAlpha2(itemscores):
    itemvars = [svar(item) for item in itemscores]
    tscores = [0] * len(itemscores[0])
    for item in itemscores:
       for i in range(len(item)):
          tscores[i]+= item[i]
    nitems = len(itemscores)
    #print "total scores=", tscores, 'number of items=', nitems

    Calpha=nitems/(nitems-1.) * (1-sum(itemvars)/ svar(tscores))
    output= print('The score of the', nitems, 'itmes is', Calpha)

    return output