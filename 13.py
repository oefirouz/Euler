FILENAME = '13.txt'
f = open(FILENAME, 'r')
numArray = []
bigSum = 0
for line in f:
    bigSum += int(line)
print str(bigSum)[0:10]
f.close()
