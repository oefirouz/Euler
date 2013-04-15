#!/usr/bin/python3.2

n = 1000
def repeatLength(x):
    modList = x*[0]
    r = 1
    place = 1
    while 1:
        r = 10*r % x
        if r == 0:
            return 0
        elif r == 1:
            return place
        elif modList[r] != 0:
            return place - modList[r]
        else:
            modList[r] = place
            place += 1
best = 0
for d in range(1,n):
    cur = repeatLength(d)
    if cur > best:
        best = cur
        bestd = d
print(bestd)
