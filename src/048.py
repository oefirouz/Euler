n = 1000
digits = 10
modVal = 10**10

def modExp(a,b,m):
    if b == 1:
        return a % m
    elif b % 2 == 0:
        return (modExp(a,b/2,m)**2) % m
    else:
        return (modExp(a,1,m)*(modExp(a,b/2,m)**2)) % m

digits = 0
for i in range(1,n+1):
    digits = (digits + modExp(i,i,modVal)) % modVal
print digits
