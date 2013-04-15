#!/usr/bin/python3.2
# The idea is to create a graph and run a topological sort.
# Since it is acyclic, there are no duplicates in the code.

f = open('079.txt')

G = { i:{} for i in range(0,10) }

for line in f:
    pin = [int(num) for num in line if num != '\n']
    G[pin[0]][pin[1]] = 1
    G[pin[0]][pin[2]] = 1
    G[pin[1]][pin[2]] = 1

def topologicalSort(graph):
    degrees = {node:0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            degrees[neighbor] += 1

    startNodes = []
    for node in degrees:
        if degrees[node] == 0 and len(graph[node]) > 0:
            startNodes.append(node)

    sort = []
    while len(startNodes) > 0:
        sort.append(startNodes.pop())
        for neighbor in G[sort[-1]]:
            degrees[neighbor] -= 1
            if degrees[neighbor] == 0:
                startNodes.append(neighbor)

    return sort

print(''.join([str(s) for s in topologicalSort(G)]))
#for 