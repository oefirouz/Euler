#!/usr/bin/python3.2
import math
N = 1000000

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

best = 20
prime = 0

for i in range(0, len(primeList)//best):
    for j in range(i + best, 5*len(primeList)//best):
        cur = sum(primeList[i:j+1])
        if (cur < N):
            if isPrime[cur]:
                best = j - i + 1
                prime = cur
print(prime)