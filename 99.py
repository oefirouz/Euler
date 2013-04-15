#!/usr/bin/python3.2
import math
FILENAME = '99.txt'

lines = open(FILENAME).readlines()
numPairs = [[int(line.split(',')[0]), int(line.split(',')[1])] for line in lines]
logVal = [pair[1]*math.log(pair[0]) for pair in numPairs]
print(logVal.index(max(logVal)) + 1)