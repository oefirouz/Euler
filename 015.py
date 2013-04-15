n = 20

numPaths = []
for i in range(0, n + 1):
    numPaths.append([1]*(n+1))

for i in range(1, n + 1):
    numPaths[i][i] = 2*numPaths[i-1][i]
    for j in range(i + 1, n + 1):
        numPaths[i][j] = numPaths[i-1][j] + numPaths[i][j-1]

print numPaths[n][n]
