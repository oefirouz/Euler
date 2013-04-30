#!/usr/bin/python3.2

N = 1000000
M = 60


factCache = {0:1, 1:1}
factOfDigitsCache = {}

def factorial(n):
    if n not in factCache:
        factCache[n] = n*factorial(n-1)
    return factCache[n]

def factOfDigits(n):
    if n not in factOfDigitsCache:
        factOfDigitsCache[n] = sum([factorial(int(i)) for i in str(n)])
    return factOfDigitsCache[n]

def seqLength(n):
    hist = {}
    while n not in hist:
        hist[n] = 1
        n = factOfDigits(n)
    return len(hist)

count = 0
for i in range(2, N+1):
    if seqLength(i) == 60: count += 1

print(count)