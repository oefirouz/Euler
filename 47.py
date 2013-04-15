#!/usr/bin/python3.2
import math
N = 500000

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

def primeFactors(x, primeList):
    factors = []
    for i in primeList:
        if i > x:
            break
        elif x % i == 0:
            f = 0
            while x % i == 0:
                f += 1
                x = x//i
            factors.append((i,f))
    return factors

isPrime, primeList = primeSieve(N)

a = set([1,2,3])
b = set([2,5])
c = set([3])

w = primeFactors(5, primeList)
x = primeFactors(4, primeList)
y = primeFactors(3, primeList)
z = primeFactors(2, primeList)
for i in range(6, N):
    z = y
    y = x
    x = w
    w = primeFactors(i, primeList)
    if (len(z) == 4 and len(y) == 4 and len(x) == 4 and len(w) == 4):
        print(i-3)
        break