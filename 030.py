upperDigits = 1
while upperDigits*(9**5) >= 10**upperDigits: upperDigits += 1
upper = 10**upperDigits

sumAll = 0
for i in xrange(2, upper):
    digSum = sum(map(lambda x: x**5, map(int, list(str(i)))))
    if i == digSum:
        sumAll += i
print sumAll
