#!/usr/bin/python3.2

N = 100
prodN = 1
prodD = 1
for n in range(10,N):
    for d in range(n+1,N):
        if n % 10 == d//10 and d % 10 != 0:
            if n/d == (n//10)/(d % 10):
                prodN *= n
                prodD *= d
        elif (n % 10) != 0 and n//10 == d % 10:
            if n/d == (n % 10)/(d // 10):
                prodN *= n
                prodD *= d

for i in range(2, prodN + 1):
    while prodN % i == 0 and prodD % i == 0:
        prodN = prodN//i
        prodD = prodD//i
print(prodD)
