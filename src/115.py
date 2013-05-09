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
def count(minSize, totalLength):
    numWays = 1  # All black.
    for position in range(totalLength + 1 - minSize):
        for size in range(minSize, totalLength + 1 - position):
            numWays += count(minSize, totalLength - 1 - position - size)
    return numWays

i = 50
while count(50, i) <= 1000000: i += 1
print(i)