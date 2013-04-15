n = 10000000

arrivalList = n*[0]
arrivalList[1] = 1
arrivalList[89] = 89

def squareSum(x):
    k = 0
    while x > 0:
        k += (x % 10)**2
        x = x//10
    return k

def numberChain(x):
    if arrivalList[x] == 0:
        arrivalList[x] = numberChain(squareSum(x))
    return arrivalList[x]

arrive89 = 0
for i in xrange(1,n):
    if numberChain(i) == 89:
        arrive89 += 1
print arrive89
