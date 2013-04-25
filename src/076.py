#!/usr/bin/python3.2

N = 100

cache = {}
def count(n, upper):
    if n == 1 or n == 0: return 1
    if upper == 1: return 1
    if (n,upper) in cache: return cache[(n,upper)]

    total = 0
    lower = min(n,upper)
    for i in range(1,lower+1):
        total += count(n-i, i)
    cache[(n,upper)] = total
    return total

print(count(100,100) - 1)