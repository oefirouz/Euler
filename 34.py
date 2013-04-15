fact = 10*[1]
for i in range(1,10):
    fact[i] = fact[i-1]*i

def factorial(x):
    return fact[x]

upperDigits = 1
while upperDigits*fact[9] >= 10**upperDigits: upperDigits += 1

sumAll = 0
upper = (upperDigits-1)*fact[9]
for i in xrange(10, upper):
    if i == sum(map(factorial, map(int, list(str(i))))):
        sumAll += i
print sumAll
