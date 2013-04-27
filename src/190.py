#!/usr/bin/python3.2

def P(m):
    prod = 1
    for i in range(1,m+1):
        prod *= ((2*i)/(m+1))**i    #Uses Lagrangian Multiplier
    return int(prod)

print(sum([P(i) for i in range(2,16)]))