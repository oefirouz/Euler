#!/usr/bin/python3.2

N = [1, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6]
d = 1
for n in N:
    count = 0
    base = 1
    while count + int(base*.9*(10**base)) < n:
        count += int(base*.9*(10**base))
        base += 1
    num = 0
    while count + base < n:
        num += 1
        count += base

    digit = 0
    while count + 1 < n:
        count += 1
        digit += 1
    d *= int(str((10**(base-1)) + num)[digit])
print(d)
