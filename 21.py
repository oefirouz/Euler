n = 10000

divisorSumDict = {}
def divisorSum(x):
    if x not in divisorSumDict:
        curSum = 1
        for i in range(2,int(x/2)+1):
            if x % i == 0:
                curSum += i
        divisorSumDict[x] = curSum
    return divisorSumDict[x]

amicableSum = 0
for i in range(2,n):
    if i == divisorSum(divisorSum(i)) and i != divisorSum(i):
        amicableSum += i

print amicableSum
