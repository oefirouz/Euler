#Uses the solution to a Diophantine Equation, http://en.wikipedia.org/wiki/Pell's_equation

b = 85
n = 120
N = 10**12

while n < N:
   b,n = 3*b+2*n-2, 4*b+3*n-3
print(b)