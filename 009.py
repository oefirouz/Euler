n = 1000
for a in range(1, int(n/3) + 1):
    for b in range(a+1, int(2*n/3) + 1):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print a*b*c
            break
