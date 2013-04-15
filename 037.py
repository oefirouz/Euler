#!/usr/bin/python3.2
import math
nGuess = 100000

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

isPrime = primeSieve(nGuess)

def trunPrime(x):
    xR = x // 10
    while xR > 0:
        if isPrime[xR]:
            xR = xR // 10
        else:
            return 0
    xL = x % (10**int(math.log10(x)))
    while xL > 0:
        if isPrime[xL]:
            xL = xL % (10**int(math.log10(xL)))
        else:
            return 0
    return 1 

num = 0
i = 10
Sum = 0
while num < 11:
    if i > nGuess:
        nGuess *= 2
        isPrime = primeSieve(nGuess)
    if isPrime[i]:
        if trunPrime(i):
            num += 1
            Sum += i
    i += 1
print(Sum)
