n = 100

print sum(map(int, list(str(reduce(lambda x, y: x*y, range(1,n))))))
