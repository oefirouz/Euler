n = 1001 #n must be odd

s = 1
for i in range(3, n+1, 2):
    s += 4*i**2 - 6*i + 6

print s
