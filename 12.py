import math
n = 500

divisorsDict = {1: set([1]), 2: set([1,2]), 3: set([1,3])}
def divisors(x):
    if x not in divisorsDict:
        divisorsDict[x] = set([1,x])
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                divisors(x/i)
                divisors(i)
                divisorsDict[x] = divisorsDict[x].union(divisorsDict[x/i].union(divisorsDict[i]))
    return len(divisorsDict[x])

i = j = 1
while divisors(i) <= n:
    j += 1
    i += j
print i
