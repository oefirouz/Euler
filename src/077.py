#!/usr/bin/python3.2

from math import sqrt

def primes(n):
    primeList = [2]
    for i in range(3,n+1,2):
        upper = sqrt(i)
        for j in primeList:
            if j > upper:
                primeList.append(i)
                break
            if i % j == 0:
                break
    return primeList


primeList = primes(100)
def count(n, upper):
    if n == 1: return 0
    if n == 0: return 1

    total = 0
    for prime in primeList:
        if (prime > upper) or (prime > n): break
        total += count(n-prime, prime)
    return total

i = 0
while count(i,i) <= 5000: i += 1
print(i)