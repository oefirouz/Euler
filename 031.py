#!/usr/bin/python3.2

#coins = [1, 2, 5, 10, 20, 50, 100, 200]
#combList = []
#for i in range(0,coins[-1]+1):
#    combList.append([-1]*(len(coins) + 1))
#
#def numComb(x,y):
#    if x == 1 or x == 0 or y == 1:
#        return 1
#    elif combList[x][y] != -1:
#        return combList[x][y]
#    else:
#        subComb = 0
#        for i in range(0, y):
#            if coins[i] <= x:
#                subComb += numComb(x - coins[i],i+1)
#        combList[x][y] = subComb
#        return subComb
#print(numComb(200, len(coins)))
count = 0
for a in range(200, -1, -200):
    for b in range(a, -1, -100):
        for c in range(b, -1, -50):
            for d in range(c, -1, -20):
                for e in range(d, -1, -10):
                    for f in range(e, -1, -5):
                        for g in range(f, -1, -2):
                            count += 1
print(count)
