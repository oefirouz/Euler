#!/usr/bin/python3.2

raw_matrix = open('081.txt', 'r').read().splitlines()
matrix = {}

for (i,line) in enumerate(raw_matrix):
    matrix[i] = {}
    for (j,num) in enumerate(line.split(',')):
        matrix[i][j] = int(num)


def memoize(function):
    cache = {}
    def decorated(*args):
        args = tuple(args)
        if args not in cache:
            cache[args] = function(*args)
        return cache[args]
    return decorated

@memoize
def partialSum(x,y):
    if (x == 0) and (y == 0):
        return matrix[x][y]
    if (x == 0):
        return matrix[x][y] + partialSum(x,y-1)
    if (y == 0):
        return matrix[x][y] + partialSum(x-1,y)
    else:
        return matrix[x][y] + min(partialSum(x-1,y), partialSum(x,y-1))

print(partialSum(len(matrix)-1, len(matrix)-1))