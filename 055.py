#!/usr/bin/python3.2
n = 10000

def isLychrel(x, depth):
    if depth == 50:
        return 1
    xx = x + int(str(x)[::-1])
    if xx == int(str(xx)[::-1]):
        return 0
    return isLychrel(xx, depth + 1)

count = 0
for i in range(0, n):
    count += isLychrel(i, 1)
print(count)    
