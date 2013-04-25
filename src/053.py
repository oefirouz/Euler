#!/usr/bin/python3.2
N = 100
M = 1000000

def comb(n,r):
    if (r < n/2):
        r = n-r
    prod = 1
    for i in range(r+1,n+1):
        prod *= i
    for i in range(2,n-r+1):
        prod //= i
    return(prod)

combVal = [1]*(N+1)
for i in range(0,len(combVal)):
    combVal[i] = [1]*(N+1)

count = 0
for i in range(1,N+1):
    for j in range(1,i//2 + 1):
        combVal[i][j] = combVal[i-1][j-1] + combVal[i-1][j]
        combVal[i][i - j] = combVal[i-1][j-1] + combVal[i-1][j]
        if (combVal[i][j] > M):
            count += 2
            if (j == i/2):
                count -= 1

print(count)