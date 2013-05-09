#!/usr/bin/python3.2

def memoize(f):
    cache = {}
    def wrap(*args):
        hashable = tuple(args)
        if hashable not in cache:
            cache[hashable] = f(*args)
        return cache[hashable]
    return wrap

@memoize
def count(size, totalLength):
    numWays = 1  # All black.
    for position in range(totalLength + 1 - size):
        numWays += count(size, totalLength - position - size)
    return numWays

# -3 as this will count all black as being valid.
print(count(2,50) + count(3,50) + count(4,50) - 3)