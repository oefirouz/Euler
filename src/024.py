n = 1000000 - 1

factorial = 10*[1]
for i in range(2,10):
    factorial[i] = factorial[i-1]*i

d = 10*[0]
r = 10*[0]
for i in range(9,0,-1):
    d[i] = n//factorial[i]
    n = n % factorial[i]

numLeft = [0,1,2,3,4,5,6,7,8,9]
num = ''
for i in range(0,10):
    num += str(numLeft.pop(d.pop()))
print num
