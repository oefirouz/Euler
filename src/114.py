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
def count(totalLength):
    numWays = 1  # All black.
    for position in range(totalLength + 1 - 3):
        for size in range(3, totalLength + 1 - position):
            numWays += count(totalLength - 1 - position - size)
    return numWays

print(count(50))