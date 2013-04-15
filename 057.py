#!/usr/bin/python3.2
from fractions import Fraction

N = 1000

count = 0
cur = Fraction(1,2)

for i in range(2,N + 1):
    cur = Fraction(3*cur.denominator + cur.numerator, 2*cur.denominator + cur.numerator)
    num = cur.numerator
    den = cur.denominator
    if (len(str(num)) > len(str(den))):
        count += 1
    cur -= 1
print(count)