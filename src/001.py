N = 1000
a = 3
b = 5

n = N - 1

print ((n - n % a) + a)*(n // a)/2 + ((n - n % b) + b)*(n // b)/2 - ((n - n % (a*b)) + (a*b))*(n // (a*b))/2
