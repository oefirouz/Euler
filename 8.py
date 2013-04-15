FILENAME = '8.txt'
f = open(FILENAME, 'r')
numList = []
for line in f:
    numList += map(int, list(line[:-1]))

best = 0
for i in range(0, len(numList)-4):
    current = numList[i]*numList[i+1]*numList[i+2]*numList[i+3]*numList[i+4]
    if current > best: best = current
print best
f.close()
