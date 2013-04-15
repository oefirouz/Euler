#!/usr/bin/python3.2

import math

aMax = 100
Products = set()
for a in range(1, aMax):
    aDig = int(math.log10(a) + 1)
    b = a+1
    bDig = int(math.log10(b) + 1)
    if (aDig + bDig + int(math.log10(a*b) + 1) > 9):
        break
    else:
        while (aDig + bDig + int(math.log10(a*b) + 1) <= 9):
            if set(str(a) + str(b) + str(a*b)) == set(map(str, range(1,10))):
                Products = Products.union({a*b})
            b += 1
            bDig = int(math.log10(b) + 1)
print(sum(Products))
