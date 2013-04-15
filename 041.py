#!/usr/bin/python3.2
import math
from itertools import permutations

#note, 9,8 cannot be done because always divisible by 3

N = 7654321
NList = ['7','6','5','4','3','2','1']

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

pSieve = primeSieve(7654321)

for x in permutations(NList):
    y = int(''.join(x))
    if pSieve[y] == 1:
        print(y)
        break
