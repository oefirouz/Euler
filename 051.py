#!/usr/bin/python3.2
import math
from copy import copy
import sys
N = 999999
n = 50000

def primeSieve(x):
    isPrime = [1]*(x+1)
    isPrime[0] = isPrime[1] = 0
    for i in range(4, x + 1, 2):
        isPrime[i] = 0
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if isPrime[i]:
            for j in range(2*i, x + 1, i):
                isPrime[j] = 0
    primeList = []
    for i in range(2,len(isPrime)):
        if (isPrime[i] == 1): 
            primeList.append(i)
    return isPrime, primeList

isPrime, primeList = primeSieve(N)

primeDict = {}

for primeNum in primeList:
    if primeNum > n:
        prime = list(str(primeNum))
        candidates = set(prime)
        for replaced in candidates:
            for a in range(0, len(prime)):
                for b in range(a, len(prime)):
                    for c in range(b, len(prime)):
                            temp = copy(prime)
                            if temp[a] == replaced:
                                temp[a] = '*'
                            if temp[b] == replaced:
                                temp[b] = '*'
                            if temp[c] == replaced:
                                temp[c] = '*'
                            tempStr = ''.join(temp)

                            if tempStr not in primeDict:
                                primeDict[tempStr] = set([primeNum])
                            else:
                                primeDict[tempStr].add(primeNum)
                                if len(primeDict[tempStr]) >= 8:
                                    print(min(primeDict[tempStr]))
                                    sys.exit()