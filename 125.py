import math
n = 1e8

upperBound = int(math.sqrt(n/2))
success = set()
for start in xrange(1, upperBound - 1):
    SumOfSquares = start*start
    for next in xrange(start+1, upperBound):
        SumOfSquares += next*next
        if SumOfSquares >= 1e8:
            break
        strSum = str(SumOfSquares)
        if strSum == strSum[::-1]:
            success.add(SumOfSquares)
print sum(success)
