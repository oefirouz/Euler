#!/usr/bin/python3.2
from itertools import permutations

NList = ['9','8','7','6','5','4','3','2','1','0']
cur = 0
for x in permutations(NList):
    if int(x[3]) % 2 == 0:
        if int(''.join(x[2:5])) % 3 == 0:
            if int(''.join(x[3:6])) % 5 == 0:
                if int(''.join(x[4:7])) % 7 == 0:
                    if int(''.join(x[5:8])) % 11 == 0:
                        if int(''.join(x[6:9])) % 13 == 0:
                            if int(''.join(x[7:10])) % 17 == 0:
                                cur += int(''.join(x))
print(cur)
