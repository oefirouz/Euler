#!/usr/bin/python3.2
n = 1000

def numSol(p):
    count = 0
    for a in range(1, p//4 + 1):
        for b in range(a, p//2 + 1):
            c = p - a - b
            if a**2 + b**2 == c**2:
                count += 1
    return count

nBest = 0
pBest = 0
for p in range(0, n+1):
    n = numSol(p)
    if n > nBest:
        nBest = n
        pBest = p
print(pBest)
