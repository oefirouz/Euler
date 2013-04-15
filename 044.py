#!/usr/bin/python3.2
from math import sqrt

def pentList(n):
    tList = [0]*n
    for i in range(1,n+1):
        tList[i-1] = i*(3*i-1)//2
    return tList

def isPent(n):
    val = (1+sqrt(1+24*n))/6
    if (val - int(val) == 0):
        return True
    else:
        return False

pList = pentList(3000)
#tSet = set(tList)
best = 1000000000

for i in range(0,len(pList)-1):
    for j in range(i+1,len(pList)):
        if (pList[j]-pList[i] <= best):
            if isPent(pList[j] - pList[i]):
                if isPent(pList[j] + pList[i]):
                    best = pList[j] - pList[i]

print(best)
