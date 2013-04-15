#!/usr/bin/python3.2

def bestPandigitalProd(x):
    num = int(str(x) + str(2*x))
    b = 3
    while num < 123456789:
        num = int(str(num) + str(b*x))
        b += 1
    if num > 987654321:
        return 0
    if set(str(num)) == set(map(str, range(1,10))):
        return num
    return 0

i = 9
Best = bestPandigitalProd(i)

j = 0
while int(str(i) + str(j)) < 54321:
    cur = bestPandigitalProd(int(str(i) + str(j)))
    if cur > Best: Best = cur
    j += 1
print(Best)
