import math

n = 4000000
phi3 = ((1 + math.sqrt(5))/2)**3
Sum = a = 2
while int(a*phi3) < n:
    a = int(round(a*phi3))
    Sum += a

print Sum
