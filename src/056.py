#!/usr/bin/python3.2

n = 100

best = 0
for a in range(1,n):
    for b in range(1,n):
        val = a**b
        dSum = sum(map(int, list(str(val))))
        if dSum > best:
            best = dSum
print(best)
