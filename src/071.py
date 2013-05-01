#1/usr/bin/python3.2

D = 1000000

best = 0
bestN = 0

for d in range(2,D):
    if d % 7 != 0:
        n = int(3*d/7)
        if n/d > best:
            best = n/d
            bestN = n
print(bestN)