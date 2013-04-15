#!/usr/bin/python3.2
import math
def primes(n):
    if n < 2:
        return None
    primeList = [2];
    for i in range(3, n+1, 2):
        upperBound = math.sqrt(i)
        for j in primeList:
            if i % j == 0:
                break
            elif j > upperBound:
                primeList.append(i)
                break
    return primeList

n = 10001
m = int(15*n)  

primeList = primes(m)
print(primeList[n-1])
