#!/usr/bin/python3.2
import math
n = 1000000
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

isPrime = primeSieve(n)
primeCount = 0
for i in range(0,n):
    if isPrime[i]:
        Prime = 1
        ii = str(i)[1:] + str(i)[0]
        while ii != str(i):
            if isPrime[int(ii)]:
                ii = ii[1:] + ii[0]
            else:
                Prime = 0
                break
        primeCount += Prime
print(primeCount)
