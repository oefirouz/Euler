n = 999
best = 0
for i in xrange(0, 1000):
    for j in xrange(i, 1000):
        prod = i*j
        if prod > best:
            s = str(prod)
            if s == s[::-1]:
                best = prod
print best
