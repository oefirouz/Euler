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

n = 20
primeList = primes(n)
prod = 1
for i in range(0, len(primeList)):
    prod *= primeList[i]**int(math.log(n)/math.log(primeList[i]))
print(prod)
