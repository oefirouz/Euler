FILENAME = '011.txt'
f = open(FILENAME)
numArray = []
for line in f:
    numArray.append(map(int, line[:-1].split()))
best = 0
for i in range(0, len(numArray)):
    for j in range(0, len(numArray[0]) - 3):
        current = numArray[i][j]*numArray[i][j+1]*numArray[i][j+2]*numArray[i][j+3]
        if current > best: best = current
for i in range(0, len(numArray[0])):
    for j in range(0, len(numArray) - 3):
        current = numArray[j][i]*numArray[j+1][i]*numArray[j+2][i]*numArray[j+3][i]
        if current > best: best = current
for i in range(0, len(numArray) - 3):
    for j in range(0, len(numArray[0]) - 3):
        current = numArray[i][j]*numArray[i+1][j+1]*numArray[i+2][j+2]*numArray[i+3][j+3]
        if current > best: best = current
for i in range(0, len(numArray) - 3):
    for j in range(3, len(numArray[0])):
        current = numArray[i][j]*numArray[i+1][j-1]*numArray[i+2][j-2]*numArray[i+3][j-3]
        if current > best: best = current
print best
