#!/usr/bin/python3.2
import math

abMax = 1000
nMax = 100
pMax = nMax**2 + abMax*nMax + abMax

def primeSieve(x):
    isPrime = [1]*(x+1)
    isPrime[0] = isPrime[1] = 0
    for i in range(4, x + 1, 2):
        isPrime[i] = 0
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if isPrime[i]:
            for j in range(2*i, x + 1, i):
                isPrime[j] = 0
    return isPrime

isPrime = primeSieve(pMax)
numBest = 0
for b in range(2, abMax):
    if isPrime[b]:
        for a in range(-abMax + 1, abMax):
            curVal = b
            for n in range(1, nMax):
                curVal = max(curVal + a + 2*n - 1, 0)
                if not isPrime[curVal]:
                    if n > numBest:
                        numBest = n
                        bestAB = [a,b]
                    break
print(bestAB[0]*bestAB[1])
