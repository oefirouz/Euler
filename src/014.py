n = 1000000

collatzLength = {1:0}
def collatz(x):
    if x not in collatzLength:
        if x % 2 == 0:
            collatzLength[x] = 1 + collatz(x/2)
        else:
            collatzLength[x] = 1 + collatz(3*x + 1)
    return collatzLength[x]

bestStartingNumber = 0
bestLength = 0

for i in range(1,n):
    if collatz(i) > bestLength:
        bestLength = collatz(i)
        bestStartingNumber = i

print bestStartingNumber
