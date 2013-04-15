#!/usr/bin/python3.2

a = 28433
n = 7830457
d = 10**10

def powMod(b, e, m):
    if e == 1:
        return b % m
    elif e % 2 == 0:
        return (powMod(b, e//2, m)**2) % m
    else:
        return (powMod(b, e-1, m)*b) % m

print((a*powMod(2, n, d) + 1) % d)
