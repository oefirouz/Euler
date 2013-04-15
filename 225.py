#!/usr/bin/python3.2

count = 0
divisor = 3

while count < 124:
    divisor += 2
    dividesFlag = 0
    t1 = 1
    t2 = 1
    t3 = 3
    while ((t1 != 1) or (t2 != 1) or (t3 != 1)):
        temp = (t1 + t2 + t3) % divisor
        t1 = t2
        t2 = t3
        t3 = temp
        if (t3 == 0):
            dividesFlag = 1
            break
    if (dividesFlag == 0):
        count += 1
print(divisor)