#!/usr/bin/python3.2
adjMatrix = open('107.txt').read().splitlines()
adjMatrix = [ line.split(',') for line in adjMatrix ]
G = {}

for i,line in enumerate(adjMatrix):
    G[i] = { j:int(edge) for j,edge in enumerate(line) if edge != '-' }

def MST(G):
    membership = { i:set([i]) for i in range(0,len(G)) }
    edges = []
    cost = 0
    for i in G: edges += [ (G[i][j],i,j) for j in G[i]]

    for (edge,i,j) in sorted(edges):
        if j not in membership[i]:
            membership[i] = membership[i].union(membership[j])
            for node in membership[i]: membership[node] = membership[i]
            cost += edge
    return sum([e for e,i,j in edges])//2 - cost

print(MST(G))