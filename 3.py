import math
n = 600851475143

def primes(n):
    if n < 2:
        return None
    primeList = [2];
    for i in xrange(3, n+1, 2):
        upperBound = math.sqrt(i)
        for j in primeList:
            if i % j == 0:
                break
            elif j > upperBound:
                primeList.append(i)
                break
    return primeList

upperBound = int(math.sqrt(n))
primeList = primes(upperBound)
for prime in primeList:
    if n == prime:
        print prime
        break
    else:
        while(n % prime) == 0:
            n = n/prime
            if n == prime:
                print prime
                break
