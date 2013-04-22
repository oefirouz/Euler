#/usr/bin/python3.2
N = 1000

print(sum([2*i*((i*i-1)//(2*i)) for i in range(3,N+1)]))