#!/usr/bin/python3.2
import math
n = 28123

def sumDivisors(x):
    Sum = 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0: Sum += i + x//i
    if int(math.sqrt(x))**2 == x: Sum -= int(math.sqrt(x))
    return Sum

abundantNumbers = []
for i in range(2,n):
    if sumDivisors(i) > i:
        abundantNumbers.append(i)
L = len(abundantNumbers)

notSummable = list(range(0,n+1))
i = j = 0
while abundantNumbers[i] <= n//2:
    while (abundantNumbers[i] + abundantNumbers[j]) <= n:
        notSummable[abundantNumbers[i] + abundantNumbers[j]] = 0
        j += 1
    i += 1
    j = i
print(abundantNumbers[:10])
print(notSummable[:100])
print(sum(notSummable))
