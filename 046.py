#!/usr/bin/python3.2
import math

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

pList = [2]
pSieve = primeSieve(100000)

for i in range(3, len(pSieve), 2):
    if (pSieve[i] == 0):
        for j in pList:
            flag = False
            if math.sqrt((i - j)/2) == int(math.sqrt((i - j)/2)):
                flag = True
                break
        if flag == False:
            print(i)
            break
    else:
        pList.append(i)
