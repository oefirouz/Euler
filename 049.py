#!/usr/bin/python3.2
import math
N = 9999
n = 1000

def isPermute(a,b):
    return set(list(str(a))) == set(list(str(b)))

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

candidates = []
for i in range(0,len(primeList)-1):
    a = primeList[i]
    if a >= n:
        for j in range(i+1, len(primeList)):
            b = primeList[j]
            if 2*b - a <= N:
                if isPrime[2*b - a]:
                    if isPermute(a,b) & isPermute(a,2*b-a):
                        candidates.append([a,b,2*b-a])
print(str(candidates[1][0]) + str(candidates[1][1]) + str(candidates[1][2]))