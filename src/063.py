#!/usr/bin/python3.2
from math import log10

# The upper bound comes from solving 9**n = 10**(n-1)

print(sum(int(b*log10(a)) + 1 == b for a in range(1,10) for b in range(1, int(1/(1-log10(9)) + 1) )))