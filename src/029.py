#!/usr/bin/python3.2
n = 100
visited = {}
for a in range(2, n + 1):
    for b in range(n, 1, -1):
        cur = a**b
        if cur not in visited:
            visited[cur] = 1
print(len(list(visited)))
