#!/usr/bin/python3.2

N = 100000

cubes = [i**3 for i in range(3,N)]
cache = {}

for cube in cubes:
    hashCube = ''.join(sorted(str(cube)))
    if hashCube not in cache:
        cache[hashCube] = []
    cache[hashCube].append(cube)
    if len(cache[hashCube]) == 5:
        print(cache[hashCube][0])
        break