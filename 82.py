#!/usr/bin/python3.2

raw_matrix = open('82.txt', 'r').read().splitlines()
matrix = {}
for (i,line) in enumerate(raw_matrix):
    matrix[i] = {}
    for (j,num) in enumerate(line.split(',')):
        matrix[i][j] = int(num)

G = {(x,y):{} for x in range(0,len(matrix)) for y in range(0,len(matrix))}
G['s'] = {(x,0):matrix[x][0] for x in range(0,len(matrix))}
for i in range(0,len(matrix)):
    G[(i,len(matrix)-1)]['t'] = 0 #matrix[i][len(matrix)-1]

for y in range(0,len(matrix)):
    for x in range(0,len(matrix)):
        if y > 0: G[(y-1,x)][(y,x)] = matrix[y][x]
        if y < len(matrix) - 1: G[(y+1,x)][(y,x)] = matrix[y][x]
        if x > 0: G[(y,x-1)][(y,x)] = matrix[y][x]

def djikstra(G,s,t):
    shortestPaths = {}
    d = {x:1000000000 for x in G}
    d['s'] = 0
    d['t'] = 100000000
    while len(d) != 0:
        cur = min(d, key=d.get)
        if (cur == t): return d[cur]
        shortestPaths[cur] = d[cur]
        del d[cur]
        for neighbor in G[cur]:
            if neighbor in d:
                if d[neighbor] > shortestPaths[cur] + G[cur][neighbor]:
                    d[neighbor] = shortestPaths[cur] + G[cur][neighbor]

print(djikstra(G,'s','t'))