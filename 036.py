#!/usr/bin/python3.2
n = 1000000
Sum = 0
for i in range(1,n):
    if str(i) == str(i)[::-1]:
        if bin(i)[2::] == bin(i)[:1:-1]:
            Sum += i
print(Sum)
