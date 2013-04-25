FILENAME = '018.txt'
f = open(FILENAME, 'r')

numArray = []
for line in f:
    numArray.append(map(int, line[:-1].split()))

for i in range(1, len(numArray)):
    numArray[i][0] += numArray[i-1][0]
    numArray[i][-1] += numArray[i-1][-1]
    for j in range(1, len(numArray[i])-1):
        numArray[i][j] += max(numArray[i-1][j-1:j+1])


print max(numArray[-1])
f.close()
